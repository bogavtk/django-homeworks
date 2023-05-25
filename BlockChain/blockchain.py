import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.nonce).encode('utf-8')
        )
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, '0', 'Genesis Block')

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Пример использования
blockchain = Blockchain()

# Создание и добавление новых блоков в блокчейн
block1 = Block(1, blockchain.get_latest_block().hash, 'Data for Block 1')
blockchain.add_block(block1)

block2 = Block(2, blockchain.get_latest_block().hash, 'Data for Block 2')
blockchain.add_block(block2)

# Вывод информации о блокчейне
for block in blockchain.chain:
    print(f'Block {block.index}:')
    print(f'Timestamp: {block.timestamp}')
    print(f'Previous Hash: {block.previous_hash}')
    print(f'Hash: {block.hash}')
    print(f'Data: {block.data}')
    print()