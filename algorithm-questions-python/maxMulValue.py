def getMaxMul(arr):
	if arr == None or len(arr) < 3:
		return None

	max1,max2,max3 = float('-inf'),float('-inf'),float('-inf')
	min1,min2,min3 = float('inf'),float('inf')

	for i in range(len(arr)):

		if arr[i] > max1:
			max3 = max2
			max2 = max1
			max1 = arr[i]
		
		elif arr[i] > max2:
			max3 = max2
			max2 = arr[i]

		elif arr[i] > max2:
			max3 = max2
			max2 = arr[i]

		elif arr[i] > max3:
			max3 = arr[i]

		if arr[i] < max1:
			min2 = min1
			min1 = arr[i]

		elif arr[i] < min2:
			min2 = arr[i]

	return max(
		max1 * max2 * max3,
		max1 * min1 * min2
		)





