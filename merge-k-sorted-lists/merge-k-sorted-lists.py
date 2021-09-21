
class Solution(object):
    def mergeKLists(self, lists):
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = point = ListNode(None)

        while h:
            val, node = heapq.heappop(h)
            point.next = ListNode(val)
            point = point.next
            curNode = lists[node] = lists[node].next
            if curNode:
                heapq.heappush(h,(curNode.val,node))
        return head.next