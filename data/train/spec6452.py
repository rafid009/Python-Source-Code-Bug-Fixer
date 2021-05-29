import numpy as np 

def function(x):

	u9 = x
	j4 = 4
	paths = []
	try:
		if x >= 8:
			j4 = j4+j4
			j4 = 9/j4
			j4 = 4*u9
			paths.append(1)
		else:
			u9 = u9/1
			j4 = 3-j4
			paths.append(2)
		if j4 > 5:
			x = x+6
			u9 = 9-x
			paths.append(3)
		else:
			j4 = x-0
			x = u9/3
			j4 = u9-7
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))