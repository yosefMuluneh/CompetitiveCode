# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # initialize a dummy node to store the merged list
        dummy = ListNode()
        # initialize a pointer to track the current node of the merged list
        curr = dummy
        # use a priority queue to store the nodes from each list in ascending order of their values
        import heapq
        pq = []
        # loop through the lists and push the first node of each list into the priority queue with its value as the priority
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next

        # loop until the priority queue is empty
        while pq:
            # pop the node with the smallest value from the priority queue and append it to the merged list
            val, i = heapq.heappop(pq)
            curr.next = ListNode(val)
            curr = curr.next
            # if there is still more nodes in the i-th list, push the next node into the priority queue with its value as the priority 
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next

        return dummy.next