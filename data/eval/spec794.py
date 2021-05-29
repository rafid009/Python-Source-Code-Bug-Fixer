import numpy as np 

def function(x):

	x4 = x
	u7 = x
	paths = []
	try:
		if u7 < 7:
			x4 = 2-x4
			u7 = u7+2
			x = x4+x
			paths.append(1)
		else:
			x = x-x4
			paths.append(2)
		if x >= 5:
			u7 = 2/u7
			x4 = x4/9
			paths.append(3)
		else:
			x = 4-7
			x = 7*x
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))