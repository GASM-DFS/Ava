try:
    from src.metadata_server import MetadataServer
    from src.data_node import DataNode
except ImportError:
    from metadata_server import MetadataServer
    from data_node import DataNode

class AvaEngine:
    def __init__(self):
        self.metadata = MetadataServer()
        self.nodes = {}
        print("🚀 Ava Engine - Intelligent Routing Online")

    def add_node(self, node_id):
        self.nodes[node_id] = DataNode(node_id)
        self.metadata.register_node(node_id)

    def ingest_data(self, filename, content):
        # 1. Ask Metadata where to put the file (This is the fix!)
        allocation_response = self.metadata.create_file(filename, len(content)/1024)
        
        # 2. Extract the node ID from the metadata
        file_info = self.metadata.get_file_info(filename)
        target_node_id = file_info['node']
        
        # 3. Physically store it on that specific node
        if target_node_id in self.nodes:
            self.nodes[target_node_id].store_block(filename, content)
        else:
            print(f"❌ Error: Target node {target_node_id} not found in cluster.")
