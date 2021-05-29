import numpy as np 

def function(x):

	u9 = x
	f2 = 0
	paths = []
	try:
		if f2 < 3:
			f2 = 4+7
			paths.append(1)
		else:
			x = x-6
			x = x/5
			x = u9-0
			paths.append(2)
		if x <= 9:
			u9 = u9+u9
			paths.append(3)
		else:
			f2 = 0-4
			u9 = 7/8
			u9 = u9+u9
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