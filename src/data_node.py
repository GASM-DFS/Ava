import os
class DataNode:
    def __init__(self, node_id, storage_path="/tmp/ava_storage"):
        self.node_id = node_id
        self.storage_path = os.path.join(storage_path, node_id)
        os.makedirs(self.storage_path, exist_ok=True)
    def store_block(self, block_id, data):
        with open(os.path.join(self.storage_path, block_id), "w") as f: f.write(data)
        return True
    def read_block(self, block_id):
        path = os.path.join(self.storage_path, block_id)
        if os.path.exists(path):
            with open(path, "r") as f: return f.read()
        return "❌ Missing"
