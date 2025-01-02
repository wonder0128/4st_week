class MaxHeap:
    def __init__(self):
        self.items = [None]
    # O(log(N))
    def insert(self, value):
        # 1. 원소를 맨 끝에 추가
        self.items.append(value)
        cur_index = len(self.items) - 1

        # 1일 경우 root node라서 더 비교할것이 없음.
        while cur_index != 1:
           # 2. 부모 노드랑 비교해서 내가 더 크면 위치를 바꿈
            parent_index = cur_index // 2

            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break

        return


max_heap = MaxHeap()
max_heap.insert(3)
#    3      Level 0
#   -> [None, 3]

max_heap.insert(4)
# 1. 맨 뒤에다가 원소 삽입
#    3      Level 0
#  4        Level 1

# 2. 부모와 비교해서 자기가 높으면 자리를 바꾼다
#    4      Level 0
#  3        Level 1

# 3. 2의 과정을 부모가 더 크거나 루트 노드에 달했을때까지 반복
#    4      Level 0
#  3        Level 1
#   -> [None, 4, 3]

max_heap.insert(2)
#    4      Level 0
#  3   2    Level 1
#   -> [None, 4, 3, 2]

max_heap.insert(9)
# [None, 4, 3, 2, 9]
#     9      Level 0
#   4   2    Level 1
#  3         Level 2
#   -> [None, 9, 4, 3, 2]

print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!