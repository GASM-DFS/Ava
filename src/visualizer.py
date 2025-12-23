import plotly.graph_objects as go

class AvaVisualizer:
    def __init__(self, engine):
        self.engine = engine

    def show_distribution(self):
        """Generates an interactive Plotly chart using robust attribute detection."""
        # 1. Get nodes (handling both list and dict types)
        nodes = self.engine.metadata.node_registry
        if isinstance(nodes, dict):
            nodes = list(nodes.keys())
            
        # 2. Robust File Mapping Detection
        # Tries to find where the engine stores the (file -> node) mapping
        meta = self.engine.metadata
        file_map = getattr(meta, 'file_registry', getattr(meta, 'registry', {}))
        
        # 3. Calculate counts per node
        counts_dict = {node: 0 for node in nodes}
        for assigned_node in file_map.values():
            if assigned_node in counts_dict:
                counts_dict[assigned_node] += 1
        
        file_counts = [counts_dict[node] for node in nodes]
        
        # 4. Create the high-contrast dashboard
        fig = go.Figure(data=[
            go.Bar(
                x=nodes, 
                y=file_counts,
                text=file_counts,
                textposition='auto',
                marker_color=['#00F5FF', '#7000FF', '#FF007A', '#FFD700', '#00FF41']
            )
        ])

        fig.update_layout(
            title='🚀 Ava DFS - Storage Distribution Dashboard',
            xaxis_title='DataNode ID',
            yaxis_title='Total Files Managed',
            template='plotly_dark',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color="cyan")
        )

        fig.show()
