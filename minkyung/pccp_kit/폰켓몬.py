def solution(nums):
    answer = len(set(nums))
    if answer > len(nums)/2 :
        return int(len(nums)/2)
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))