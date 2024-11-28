import logging

from blockchain import Blockchain

logging.basicConfig(level=logging.INFO, format="%(message)s")


def main():
    block_one_transactions = [
        {"amount": 100, "sender": "Alice", "receiver": "Bob"},
        {"amount": 200, "sender": "Bob", "receiver": "Charlie"},
    ]

    block_two_transactions = [
        {"amount": 300, "sender": "Alice", "receiver": "Bob"},
        {"amount": 400, "sender": "Bob", "receiver": "Charlie"},
    ]

    block_three_transactions = [
        {"amount": 500, "sender": "Alice", "receiver": "Bob"},
        {"amount": 600, "sender": "Bob", "receiver": "Charlie"},
    ]

    fake_transactions = [
        {"amount": 700, "sender": "Alice", "receiver": "Bob"},
        {"amount": 800, "sender": "Bob", "receiver": "Charlie"},
    ]

    local_blockchain = Blockchain()

    local_blockchain.add_block(block_one_transactions)
    local_blockchain.add_block(block_two_transactions)
    local_blockchain.add_block(block_three_transactions)
    # local_blockchain.print_blocks()

    local_blockchain.add_block(fake_transactions)
    local_blockchain.validate_chain()
    local_blockchain.print_blocks()


if __name__ == "__main__":
    main()
