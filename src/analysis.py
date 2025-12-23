class AvaAnalytic:
    def __init__(self, engine):
        self.engine = engine

    def find_keyword(self, keyword):
        """Searches all DataNodes for a specific keyword."""
        print(f"🔍 Searching DFS for: '{keyword}'...")
        results = []

        # 1. Get list of files from Metadata
        for filename, metadata in self.engine.metadata.file_table.items():
            # 2. Retrieve data from the assigned node
            node_id = metadata['node']
            content = self.engine.nodes[node_id].read_block(filename)

            # 3. Analyze content
            if keyword.lower() in content.lower():
                results.append({
                    "file": filename,
                    "node": node_id,
                    "preview": content[:50] + "..."
                })

        return results

# --- Local Component Test ---
if __name__ == "__main__":
    from src.engine import AvaEngine
    # We use a dummy setup for the component test
    test_engine = AvaEngine()
    test_engine.add_node("node_1")
    test_engine.ingest_data("log.txt", "CRITICAL ERROR: Memory leak detected in DFS block 4.")

    analyzer = AvaAnalytic(test_engine)
    found = analyzer.find_keyword("CRITICAL")
    print(f"Results: {found}")
