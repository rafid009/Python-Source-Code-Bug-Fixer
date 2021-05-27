import numpy as np 

def function(x):

	u7 = x
	q8 = x
	paths = []
	try:
		if u7 > 6:
			u7 = u7/1
			q8 = 7-3
			u7 = 7*u7
			paths.append(1)
		else:
			q8 = q8-5
			x = x/u7
			paths.append(2)
		if q8 < 7:
			u7 = u7/6
			x = 9+7
			paths.append(3)
		else:
			x = x-0
			u7 = u7/6
			q8 = 8-q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))