import numpy as np 

def function(x):

	u6 = x
	y5 = x
	paths = []
	try:
		if u6 >= 8:
			x = 1+0
			paths.append(1)
		else:
			y5 = y5+x
			paths.append(2)
		if y5 <= 3:
			u6 = x/y5
			u6 = u6+u6
			y5 = 8-4
			paths.append(3)
		else:
			y5 = y5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))