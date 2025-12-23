import time
import uuid
class MetadataServer:
    def __init__(self):
        self.file_table = {}
        self.node_registry = set()
    def register_node(self, node_id):
        self.node_registry.add(node_id)
    def create_file(self, filename, size_mb):
        if not self.node_registry: return "❌ No nodes"
        file_id = str(uuid.uuid4())
        assigned_node = list(self.node_registry)[0]
        self.file_table[filename] = {"id": file_id, "size": f"{size_mb}MB", "node": assigned_node}
        return f"✅ {filename} allocated to {assigned_node}"
    def get_file_info(self, filename):
        return self.file_table.get(filename, "Not found")
