import numpy as np 

def function(x):

	q2 = x
	u9 = 7
	paths = []
	try:
		if x >= 6:
			q2 = q2/3
			paths.append(1)
		else:
			u9 = u9+9
			u9 = 8+q2
			paths.append(2)
		if q2 >= 1:
			q2 = 2/u9
			q2 = q2/x
			q2 = 3+q2
			paths.append(3)
		else:
			u9 = u9-4
			u9 = u9*6
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))