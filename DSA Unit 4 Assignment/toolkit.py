# =========================
# DMMT TOOLKIT
# =========================

# -------- BST MODULE --------
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(root, key):
            if not root:
                return BSTNode(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            else:
                root.right = _insert(root.right, key)
            return root
        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(root, key):
            if not root:
                return False
            if root.key == key:
                return True
            elif key < root.key:
                return _search(root.left, key)
            else:
                return _search(root.right, key)
        return _search(self.root, key)

    def inorder(self):
        result = []
        def _inorder(root):
            if root:
                _inorder(root.left)
                result.append(root.key)
                _inorder(root.right)
        _inorder(self.root)
        return result

    def delete(self, key):
        def _delete(root, key):
            if not root:
                return root

            if key < root.key:
                root.left = _delete(root.left, key)
            elif key > root.key:
                root.right = _delete(root.right, key)
            else:
                # Case 1: No child
                if not root.left and not root.right:
                    return None
                # Case 2: One child
                elif not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                # Case 3: Two children
                else:
                    temp = root.right
                    while temp.left:
                        temp = temp.left
                    root.key = temp.key
                    root.right = _delete(root.right, temp.key)
            return root

        self.root = _delete(self.root, key)


# -------- GRAPH MODULE --------
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor, _ in self.graph.get(node, []):
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        visited = set()
        result = []

        def _dfs(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor, _ in self.graph.get(node, []):
                    _dfs(neighbor)

        _dfs(start)
        return result


# -------- HASH TABLE --------
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False

    def display(self):
        return self.table


# -------- MAIN RUNNER --------
def main():
    with open("output.txt", "w") as f:

        # ===== BST TEST =====
        f.write("=== BST ===\n")
        bst = BST()

        nums = [50, 30, 70, 20, 40, 60, 80]
        for n in nums:
            bst.insert(n)

        f.write("Inorder: " + str(bst.inorder()) + "\n")
        f.write("Search 20: " + str(bst.search(20)) + "\n")
        f.write("Search 90: " + str(bst.search(90)) + "\n")

        # Delete cases
        bst.delete(20)  # leaf
        bst.delete(30)  # one child
        bst.delete(50)  # two children

        f.write("After Deletion: " + str(bst.inorder()) + "\n\n")

        # ===== GRAPH TEST =====
        f.write("=== GRAPH ===\n")
        g = Graph()

        edges = [
            ('A','B',2), ('A','C',4), ('B','D',7),
            ('B','E',3), ('C','E',1), ('D','F',5),
            ('E','D',2), ('E','F',6), ('C','F',8)
        ]

        for u, v, w in edges:
            g.add_edge(u, v, w)

        f.write("Adjacency List:\n")
        for k in g.graph:
            f.write(f"{k} -> {g.graph[k]}\n")

        f.write("BFS from A: " + str(g.bfs('A')) + "\n")
        f.write("DFS from A: " + str(g.dfs('A')) + "\n\n")

        # ===== HASH TABLE =====
        f.write("=== HASH TABLE ===\n")
        ht = HashTable(5)

        keys = [10, 15, 20, 7, 12]
        for k in keys:
            ht.insert(k, k*10)

        f.write("Table: " + str(ht.display()) + "\n")

        f.write("Get 10: " + str(ht.get(10)) + "\n")
        f.write("Get 7: " + str(ht.get(7)) + "\n")

        ht.delete(15)
        f.write("After deleting 15: " + str(ht.display()) + "\n")


if __name__ == "__main__":
    main()