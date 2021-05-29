import numpy as np 

def function(x):

	u9 = x
	l2 = 9
	paths = []
	try:
		if l2 >= 4:
			x = 8/4
			paths.append(1)
		else:
			u9 = x+u9
			u9 = u9/6
			u9 = 8/u9
			paths.append(2)
		if x < 9:
			x = 5-2
			paths.append(3)
		else:
			l2 = 2-4
			u9 = 8/u9
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