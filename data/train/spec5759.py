import numpy as np 

def function(x):

	x6 = 3
	u9 = x
	paths = []
	try:
		if u9 <= 0:
			x6 = x6-4
			paths.append(1)
		else:
			x6 = x+x6
			u9 = u9-0
			x = x-x6
			paths.append(2)
		if x6 <= 3:
			u9 = 6+u9
			u9 = 9+u9
			paths.append(3)
		else:
			x = 9-2
			x6 = 3+6
			x = u9*3
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