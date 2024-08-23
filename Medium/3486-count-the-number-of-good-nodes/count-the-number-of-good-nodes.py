class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        
        def dfs(node, parent):
            size = 1
            child_sizes = []
            for neighbor in tree[node]:
                if neighbor != parent:
                    subtree_size = dfs(neighbor, node)
                    child_sizes.append(subtree_size)
                    size += subtree_size
            if len(set(child_sizes)) <= 1:
                self.good_nodes += 1
            return size
        
        
        self.good_nodes = 0
        
        
        dfs(0, -1)
        
        return self.good_nodes