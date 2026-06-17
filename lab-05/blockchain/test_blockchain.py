import json
from blockchain import Blockchain

def print_block(block):
    print(f"\n================ Block {block.index} ================")
    print(f"Timestamp    : {block.timestamp}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Proof        : {block.proof}")
    print(f"Hash         : {block.hash}")
    print("Transactions :")
    if len(block.transactions) == 0:
        print("   (Không có giao dịch - Genesis Block)")
    for tx in block.transactions:
        print(f"   - {tx['sender']} -> {tx['recipient']}: {tx['amount']} coins ({tx['timestamp']})")
    print("==========================================")

def main():
    print("=== KHIỂM THỬ MÔ PHỎNG BLOCKCHAIN ===")
    
    # 1. Khởi tạo Blockchain
    print("\nKhởi tạo Blockchain mới...")
    blockchain = Blockchain()
    
    # In Block đầu tiên (Genesis Block)
    print_block(blockchain.chain[0])
    
    # 2. Thêm giao dịch và Đào Block 1
    print("\n[+] Thêm giao dịch mới vào Block 1...")
    blockchain.new_transaction(sender="Lê Viết Đức", recipient="Nguyễn Văn A", amount=50.5)
    blockchain.new_transaction(sender="Nguyễn Văn A", recipient="Trần Thị B", amount=10.0)
    
    print("Đang chạy Proof of Work để tìm Hash hợp lệ (Đang đào)...")
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)
    print(f"-> Tìm thấy Proof: {proof}")
    
    # Tạo Block 1
    block1 = blockchain.new_block(proof)
    print("Đào thành công Block 1!")
    print_block(block1)
    
    # 3. Thêm giao dịch và Đào Block 2
    print("\n[+] Thêm giao dịch mới vào Block 2...")
    blockchain.new_transaction(sender="Trần Thị B", recipient="Lê Viết Đức", amount=5.0)
    
    print("Đang chạy Proof of Work (Đang đào)...")
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)
    print(f"-> Tìm thấy Proof: {proof}")
    
    # Tạo Block 2
    block2 = blockchain.new_block(proof)
    print("Đào thành công Block 2!")
    print_block(block2)
    
    # 4. Kiểm tra tính hợp lệ của Blockchain
    print("\n--- Kiểm tra tính hợp lệ của Chuỗi Blockchain ---")
    is_valid = blockchain.is_chain_valid()
    print(f"Is Blockchain Valid: {is_valid}")
    print("-------------------------------------------------")
    
    # 5. Thử nghiệm thay đổi dữ liệu trái phép (Tấn công Blockchain)
    print("\n[Tấn Công Giả Lập] Thay đổi số tiền giao dịch tại Block 1 từ 50.5 thành 999.0...")
    blockchain.chain[1].transactions[0]['amount'] = 999.0
    
    # Tính lại hash xem hệ thống phát hiện không
    print("--- Kiểm tra tính hợp lệ sau khi bị thay đổi dữ liệu ---")
    is_valid_after_attack = blockchain.is_chain_valid()
    print(f"Is Blockchain Valid: {is_valid_after_attack}")
    print("--------------------------------------------------------")
    
    if not is_valid_after_attack:
        print("[SUCCESS] Hệ thống phát hiện dữ liệu Block 1 đã bị giả mạo và từ chối chuỗi này!")
    else:
        print("[LỖI] Hệ thống không phát hiện ra việc giả mạo dữ liệu!")

if __name__ == "__main__":
    main()
