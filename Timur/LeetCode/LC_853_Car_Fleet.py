class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        # iterate starting from the leading car (closest to target)
        for pos, spd in sorted(cars)[::-1]:
                curr_finish_time = (target - pos) / spd

                # add only in case when current car does not intersect with front car
                if (len(stack) > 0 and stack[-1] < curr_finish_time) or (len(stack) == 0):
                        stack.append(curr_finish_time)
        return len(stack)
