import time
import uuid

class MetadataServer:
    def __init__(self):
        self.file_table = {}
        self.node_registry = [] # Changed to list for ordered rotation
        self.last_node_index = -1
        print("🔧 Metadata Server (Ava Engine) - Load Balancer Active")

    def register_node(self, node_id):
        """Adds a DataNode to the system pool."""
        if node_id not in self.node_registry:
            self.node_registry.append(node_id)
            print(f"📡 Node {node_id} joined the cluster.")

    def _get_next_node(self):
        """Simple Round Robin Load Balancing logic."""
        if not self.node_registry:
            return None
        self.last_node_index = (self.last_node_index + 1) % len(self.node_registry)
        return self.node_registry[self.last_node_index]

    def create_file(self, filename, size_mb):
        """Assigns a file to nodes using Round Robin distribution."""
        assigned_node = self._get_next_node()
        if not assigned_node:
            return "❌ Error: No storage nodes available."
        
        file_id = str(uuid.uuid4())
        self.file_table[filename] = {
            "id": file_id,
            "size": f"{size_mb}MB",
            "node": assigned_node,
            "created_at": time.ctime()
        }
        return f"✅ File '{filename}' allocated to {assigned_node}."

    def get_file_info(self, filename):
        return self.file_table.get(filename, "File not found.")
