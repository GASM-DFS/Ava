from src.metadata_server import MetadataServer
from src.data_node import DataNode
class AvaEngine:
    def __init__(self):
        self.metadata = MetadataServer()
        self.nodes = {}
    def add_node(self, node_id):
        self.nodes[node_id] = DataNode(node_id)
        self.metadata.register_node(node_id)
    def ingest_data(self, filename, content):
        self.metadata.create_file(filename, len(content)/1024)
        if self.nodes:
            target = list(self.nodes.keys())[0]
            self.nodes[target].store_block(filename, content)
