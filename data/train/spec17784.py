import numpy as np 

def function(x):

	u6 = 3
	i0 = 1
	paths = []
	try:
		if x >= 1:
			u6 = x+2
			x = x*i0
			paths.append(1)
		else:
			x = u6*x
			i0 = i0+5
			paths.append(2)
		if x <= 5:
			u6 = 6+u6
			paths.append(3)
		else:
			u6 = 6/u6
			i0 = i0+5
			u6 = 6/i0
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