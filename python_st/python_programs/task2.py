# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         left,right=0,len(height)-1
#         # max=height[0]
#         total=[]
#         while left <right:
#             currentsum=height[left]*height[right]
#             left+=1
#             right-=1
#             total.append(currentsum)
#             # if total >max:
#             #     max=total
#             # return max # Placeholder, replace with your actual result
#             print(total)

# # Test cases
# solver = Solution()

# # Test Case 1
# height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(f"Input: {height1} -> Output: {solver.maxArea(height1)}") # Expected: 49

# # Test Case 2
# height2 = [1, 1]
# print(f"Input: {height2} -> Output: {solver.maxArea(height2)}") # Expected: 1

# # Test Case 3
# height3 = [4, 3, 2, 1, 4]
# print(f"Input: {height3} -> Output: {solver.maxArea(height3)}") # Expected: 16 (lines at 0 and 4, height=4, width=4)

# # Test Case 4
# height4 = [1, 2, 1]
# print(f"Input: {height4} -> Output: {solver.maxArea(height4)}") # Expected: 2 (lines at 0 and 2, height=1, width=2)

# # Test Case 5 (Descending order)
# height5 = [7, 6, 5, 4, 3, 2, 1]
# print(f"Input: {height5} -> Output: {solver.maxArea(height5)}") # Expected: 12 (lines at 0 and 6, height=1, width=6) OR (lines at 0 and 1, height=6, width=1) -> 7*1 = 7
#                                                                 # Correct: (7 and 1 line) = 1*6 = 6. (6 and 2 line) = 2*4 = 8. (7 and 6 line) = 6*1 = 6. Max for [7,6,5,4,3,2,1] should be between 7 and 1, area is 1 * 6 = 6.
#                                                                 # Let's recheck this test case: [7,6,5,4,3,2,1]
#                                                                 # L=0 (7), R=6 (1). Area = min(7,1)*(6-0) = 1*6 = 6
#                                                                 # Move R. L=0 (7), R=5 (2). Area = min(7,2)*(5-0) = 2*5 = 10
#                                                                 # Move R. L=0 (7), R=4 (3). Area = min(7,3)*(4-0) = 3*4 = 12
#                                                                 # Move R. L=0 (7), R=3 (4). Area = min(7,4)*(3-0) = 4*3 = 12
#                                                                 # Move R. L=0 (7), R=2 (5). Area = min(7,5)*(2-0) = 5*2 = 10
#                                                                 # Move R. L=0 (7), R=1 (6). Area = min(7,6)*(1-0) = 6*1 = 6.
#                                                                 # Max is 12.
# # Corrected Expected Output for Test Case 5:
# # height5 = [7, 6, 5, 4, 3, 2, 1]
# # print(f"Input: {height5} -> Output: {solver.maxArea(height5)}") # Expected: 12
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        
        # Start max_area at 0.
        max_area = 0 
        
        while left < right:
            # 1. Correct Area Formula
            # Width = right - left
            # Height = min(height[left], height[right])
            width = right - left
            current_height = min(height[left], height[right])
            current_area = current_height * width
            
            # 2. Update the max area if this one is bigger
            if current_area > max_area:
                max_area = current_area
                
            # 3. Correct Pointer Movement
            # We move the *shorter* line's pointer inward.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        # After the loop finishes, return the biggest area found.
        return max_area

# --- Test ---
solver = Solution()
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"Heights: {heights}")
print(f"Max Area: {solver.maxArea(heights)}") # Output: 49