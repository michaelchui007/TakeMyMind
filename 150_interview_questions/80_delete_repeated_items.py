from typing import List


class Solution:
	"""
	给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
	不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
	"""
	"""
	整体思路：
	1、设定一个flag用来判断重复次数、设定一个location用来赋值并最终作为length返回、设定一个temp_num用来读取比较的数字
	2、遍历数组：
	如果当前值等于temp_num
		如果flag < 2，location + 1，flag+1
		否则，下一道循环
	如果不等于temp_num
		temp_num赋值，location + 1， 数组值更新
	"""

	def removeDuplicates(self, nums: List[int]) -> int:
		flag = 0
		location = 0
		temp_num = -1
		for num in nums:
			if num == temp_num:
				if flag < 1:
					nums[location] = num
					location += 1
					flag += 1
				else:
					continue
			else:
				flag = 0
				temp_num = num
				nums[location] = num
				location += 1
		return location


solution = Solution()

if __name__ == '__main__':
	nums = [1, 1, 1, 2, 2, 3]
	# nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

	return1 = solution.removeDuplicates(nums)
	print(f"\n{return1}")
	print(nums)
