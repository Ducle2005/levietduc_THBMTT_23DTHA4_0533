import time
import hashlib
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.difficulty = 4  # Số chữ số 0 đứng đầu yêu cầu khi đào block (độ khó)

        # Tạo Genesis Block (Block đầu tiên của chuỗi)
        self.new_block(proof=100, previous_hash='1')

    def new_block(self, proof, previous_hash=None):
        """Tạo một Block mới và thêm vào chuỗi"""
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time.time(),
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=previous_hash or self.chain[-1].hash
        )

        # Reset danh sách các giao dịch hiện tại
        self.current_transactions = []
        
        # Thêm block vào chuỗi
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """Thêm giao dịch mới vào danh sách giao dịch chờ đào"""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'timestamp': time.time()
        })
        return self.last_block.index + 1

    @property
    def last_block(self):
        """Lấy Block cuối cùng trong chuỗi"""
        return self.chain[-1]

    def proof_of_work(self, last_block):
        """
        Thuật toán Proof of Work (Mô tả quá trình đào):
        Tìm một số proof sao cho hash(last_proof, proof, last_hash) có đúng số số 0 đứng đầu bằng độ khó.
        """
        last_proof = last_block.proof
        last_hash = last_block.hash
        proof = 0
        
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1
            
        return proof

    def valid_proof(self, last_proof, proof, last_hash):
        """Kiểm tra xem mã băm có thỏa mãn độ khó hay không"""
        guess = f'{last_proof}{proof}{last_hash}'.encode('utf-8')
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:self.difficulty] == '0' * self.difficulty

    def is_chain_valid(self):
        """Kiểm tra tính hợp lệ toàn bộ blockchain"""
        last_block = self.chain[0]
        current_index = 1

        while current_index < len(self.chain):
            block = self.chain[current_index]
            
            # 1. Kiểm tra Previous Hash có khớp với Hash thực tế của block trước đó không
            if block.previous_hash != last_block.hash:
                print(f"[-] Lỗi tính toàn vẹn: Block {block.index} có previous_hash không khớp với hash của Block {last_block.index}")
                return False

            # 2. Kiểm tra Proof of Work có hợp lệ không
            if not self.valid_proof(last_block.proof, block.proof, last_block.hash):
                print(f"[-] Lỗi Proof of Work: Block {block.index} có proof {block.proof} không hợp lệ")
                return False
                
            # 3. Kiểm tra tính đúng đắn của băm nội tại block
            if block.hash != block.calculate_hash():
                print(f"[-] Lỗi băm nội tại: Block {block.index} có dữ liệu bị thay đổi sau khi tạo")
                return False

            last_block = block
            current_index += 1

        return True
