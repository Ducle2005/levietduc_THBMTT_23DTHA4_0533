import hashlib
import json

class Block:
    def __init__(self, index, timestamp, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Tính toán mã băm SHA-256 của Block hiện tại"""
        # Sắp xếp các transaction theo key để đảm bảo tính nhất quán của chuỗi JSON
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'proof': self.proof,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode('utf-8')
        
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self):
        """Chuyển đổi block thành dictionary phục vụ in ấn"""
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'proof': self.proof,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }
