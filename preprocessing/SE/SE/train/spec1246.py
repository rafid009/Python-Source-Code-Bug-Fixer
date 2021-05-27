import numpy as np 

def function(x):

	u9 = x
	y2 = 5
	paths = []
	try:
		if u9 < 0:
			u9 = u9+y2
			paths.append(1)
		else:
			u9 = u9-5
			u9 = y2/x
			u9 = 2*2
			paths.append(2)
		if u9 >= 1:
			x = 3+y2
			y2 = x*y2
			paths.append(3)
		else:
			u9 = x+0
			x = x+x
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