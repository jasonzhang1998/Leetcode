# 序列化二叉树


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 将树编码为层序遍历序列，需编码空节点
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        vals = data[1:-1].split(',')
        i = 1
        root = TreeNode(int(vals[0]))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


x = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root = None
print(x.serialize(root))

y = x.deserialize(x.serialize(root))
print(y.left.val)
