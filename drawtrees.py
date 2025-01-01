from drawtree import draw_level_order


class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def fromList(lst):
        if not lst:
            return None
        root = Tree(lst[0])
        queue = [root]
        i = 1
        while i < len(lst):
            node = queue.pop(0)
            if lst[i] is not None:
                node.left = Tree(lst[i])
                queue.append(node.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                node.right = Tree(lst[i])
                queue.append(node.right)
            i += 1
        return root
    def toList(self):
        if not self:
            return []
        result = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result
    
root = Tree.fromList([3,5,2,1,4,6,None,7,8,None,None,9,10,11,12,13,14])
draw_level_order(f"{root.toList()}")
