class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        result, Queue, temp = [root.val], [root], []
        while Queue:
            for i in Queue:
                if i.left: 
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if temp:
                result.append(temp[-1].val)
            Queue, temp = temp, []
        return result