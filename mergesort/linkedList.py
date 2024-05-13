class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def iter(self):
        curr = self
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

class LinkedList:
    def __init__(self, arr=[]) -> None:
        self.head = None
        if arr:
            self.build(arr)

    def __len__(self):
        n = 0
        curr = self.head
        while curr:
            n += 1
            curr = curr.next
        return n

    def build(self, arr):
        if not arr:
            return
        dummy = ListNode()
        curr = dummy
        for v in arr:
            node = ListNode(v)
            curr.next = node
            curr = curr.next
        self.head = dummy.next

    def get_array(self):
        arr = []
        if self.head:
            curr = self.head
            while curr:
                arr.append(curr.val)
                curr = curr.next
        return arr

# bottom-up
# Time: O(3NlogN)
# Space: O(1)
class Solution2:
    def mergeSort(self, head):
        # bottom-up
        # _. _. _. _. _. _. ...
        # for each width=1*2*2..
        #   merge consecutive two 
        n = self.get_length(head) # O(N)
        width = 1

        # width = 1, 2, 4, ...
        while width < n: # O(logN)
            dummy = ListNode()
            curr = dummy
            firstHead = head
            secondHead = None
            tail = dummy

            while firstHead: 
                secondHead = self.get_split(firstHead, width) # node, None, O(N)
                tail = self.get_split(secondHead, width) # node, None, O(N)
                mergedHead, mergedEnd = self.merge(firstHead, secondHead) # O(N)
                curr.next = mergedHead
                curr = mergedEnd
                firstHead = tail

            width = 2*width
            head = dummy.next
        
        return head
    
    def get_split(self, head, step):
        'return the start of next half'
        if not head:
            return head
        prev = None
        curr = head
        for i in range(step):
            if not curr:
                break
            prev = curr if not prev else prev.next
            curr = curr.next
        prev.next = None
        return curr

    def merge(self, firstStart, secondStart):
        'firstStart: node, secondStart: node, none'
        dummy = ListNode()
        curr = dummy
        while firstStart and secondStart:
            if firstStart.val < secondStart.val:
                curr.next = firstStart
                firstStart = firstStart.next
            else:
                curr.next = secondStart
                secondStart = secondStart.next
            curr = curr.next
        curr.next = firstStart if firstStart else secondStart

        prev = None
        while curr:
            prev = curr if not prev else prev.next
            curr = curr.next

        return dummy.next, prev
        
    def get_length(self, head):
        if not head:
            return 0
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        return n

# top-down
# Time: O(2NlogN)
# Space: O(NlogN)
class Solution:
    def mergeSort(self, head): # O(logN)
        if head is None or head.next is None:
            return head

        # split
        mid = self.get_mid(head) # O(N)

        # recursive merge
        left = self.mergeSort(head)
        right = self.mergeSort(mid)
        merged_head = self.merge(left, right) # O(N)

        return merged_head

    def get_mid(self, head):
        curr = head
        prev = None
        while curr and curr.next:
            prev = curr if not prev else prev.next
            curr = curr.next.next
        mid = prev.next
        prev.next = None
        return mid

    def merge(self, left, right):
        dummy = ListNode()
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
        return dummy.next



# Test functions

def isSameList(list1,list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

def run_test(testcase, i=0):
    inputList = LinkedList(testcase[0])

    sol = Solution2()
    sorted_head = sol.mergeSort(inputList.head)
    res = sorted_head.iter()

    print(f'Testcase{i+1}: {testcase[0]}')
    print(f'Result: {res}')
    isCorrect = isSameList(res, testcase[1])
    print(isCorrect)

    return isCorrect


testcases = [
    [[4,2,1,3], [1,2,3,4]],
    [[1,23,40,11, 4,2,1,3], [1, 1, 2, 3, 4, 11, 23, 40]]
]

print('==== Running Test Cases ====\n')
success = 0
for i, case in enumerate(testcases):
    if run_test(case, i):
        success += 1
    print()

n = len(testcases)
print(f"Success: {success}/{n}, Failed: {n-success}/{n}")
print('==== END ====')
