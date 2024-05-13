#test cases
# Problem
# Given a list of hosts, each having a capacity and a list of scheduled jobs
# And a new task with desired time
# Find the host that could fit the new task, rank by smallest capacity if multiple hosts exist

import math

def getTestCase(index):
    cases=[
        {
            "hosts": [
                (5, [[1,2], [4,6], [7, 9]]),
                (10, [[1,2], [6,7]]),
                (5, [[3,6]])
            ],
            "task": (5, [3,4]),
            "result": 2
        },
        {
            "hosts": [
                (5, [[1,10], [42,45],[100, 200]]),
                (10, [[100, 200]]),
                (5, [[30, 40]])
            ],
            "task": (5, [41, 57]),
            "result": 3
        }
    ]

    selected = cases[index-1]
    hosts = {}
    for i, h in enumerate(selected['hosts']):
        hosts[f'Host{i+1}'] = {
            'capacity': h[0],
            'times': h[1]
        }

    task = {
        'capacity': selected['task'][0],
        'times': selected['task'][1]
    }

    return {
        "hosts": hosts, "task": task, 'result': f'Host{selected['result']}'
    }


# expected result: "host2"
def isConflict(schedules, target):
    # O(len(schedules))
    for schedule in schedules:
        if not (target[0] > schedule[1] or target[1] < schedule[0]):
            return True
    return False

def isConflict2(schedules, target, debug=False):
    def condition(mid_val, target_val):
        return mid_val >= target_val
    
    left, right = 0, len(schedules)
    while left < right:
        mid = left + (right - left)//2
        if condition(schedules[mid][0], target[0]):
            right = mid
        else:
            left = mid + 1
    if debug:
        print(schedules, target)
        print(left)

    # special case, left = 0
    if left == 0 and target[1] >= schedules[0][0]:
        if debug:
            print('left==0 -> overlap')
        return True
    
    # special case, left = n-1
    if left == len(schedules) and target[0] <= schedules[-1][1]:
        if debug:
            print('right=n -> overlap')
        return True
    
    # common, start falls between all open brackets' start
    if (left > 0 and left < len(schedules)) and not (target[0] > schedules[left-1][1] and target[1] < schedules[left][0]):
        if debug:
            print('common -> overlap')
        return True
    
    if debug:
        print('no overlap')
    return False

def Solution(hosts, task, method=1, debug=False):
    res = None
    res_capacity = math.inf
    for hostName, hostConfig in hosts.items():
        if method == 1:
            isOverlap = isConflict(hostConfig['times'], task['times'])
        else:
            isOverlap = isConflict2(hostConfig['times'], task['times'], debug)


        isAvailable = (not isOverlap) and (task['capacity'] <= hostConfig['capacity'])
        # if capacity is equal, rank by lexicography
        if isAvailable and (hostConfig['capacity'] < res_capacity or hostName < res):
            res = hostName
            res_capacity = hostConfig['capacity']
    return res

def test(testCaseIndex, method, debug):

    print(f'Test Case {testCaseIndex}')

    testCase = getTestCase(testCaseIndex)
    debug = (debug==1)

    result = Solution(testCase['hosts'], testCase['task'], method, debug)
    if result == testCase['result']:
        print('Pass')
    else:
        print('Fail')
    print('details:', result, testCase['result'])

test(2, 2, 0)