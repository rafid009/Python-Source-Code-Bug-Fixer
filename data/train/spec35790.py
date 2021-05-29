import numpy as np 

def function(x):

	x4 = 2
	u6 = 5
	paths = []
	try:
		if u6 >= 7:
			x = x4+x
			x4 = x/x4
			paths.append(1)
		else:
			x4 = x4*5
			u6 = 7+0
			paths.append(2)
		if x >= 0:
			x = x+5
			paths.append(3)
		else:
			u6 = u6/7
			u6 = 2*4
			x4 = 9/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))