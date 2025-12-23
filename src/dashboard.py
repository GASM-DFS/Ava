class AvaDashboard:
    def __init__(self, engine):
        self.engine = engine

    def generate_report(self):
        """Generates a summary of the DFS Health."""
        print("\n" + "="*40)
        print("📊 AVA DFS HEALTH DASHBOARD")
        print("="*40)
        
        # 1. Node Statistics
        node_count = len(self.engine.nodes)
        print(f"📡 Active DataNodes: {node_count}")
        
        # 2. File Statistics
        file_count = len(self.engine.metadata.file_table)
        print(f"📁 Total Files Managed: {file_count}")
        
        # 3. Storage Distribution
        print("\n📍 Storage Distribution:")
        distribution = {}
        for filename, meta in self.engine.metadata.file_table.items():
            # Basic error handling for missing metadata
            if isinstance(meta, dict):
                node = meta.get('node', 'unknown')
                distribution[node] = distribution.get(node, 0) + 1
            
        for node, count in distribution.items():
            print(f"   - {node}: {count} files")
            
        print("="*40 + "\n")

# --- Local Component Test ---
if __name__ == "__main__":
    from src.engine import AvaEngine
    engine = AvaEngine()
    engine.add_node("alpha_node")
    engine.add_node("beta_node")
    engine.ingest_data("test1.txt", "data")
    engine.ingest_data("test2.txt", "data")
    
    dash = AvaDashboard(engine)
    dash.generate_report()
