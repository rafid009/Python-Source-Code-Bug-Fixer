import numpy as np 

def function(x):

	p9 = 9
	u9 = x
	x = 9
	paths = []
	try:
		if u9 >= 6:
			p9 = 4/x
			u9 = u9/x
			paths.append(1)
		else:
			x = x-6
			x = 2-x
			paths.append(2)
		if u9 >= 6:
			p9 = 4-2
			u9 = u9/u9
			paths.append(3)
		else:
			u9 = 4/u9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))