import numpy as np 

def function(x):

	u6 = 2
	n9 = 8
	paths = []
	try:
		if n9 <= 6:
			x = x*4
			n9 = 3/x
			u6 = u6*7
			paths.append(1)
		else:
			n9 = u6+7
			x = x-5
			paths.append(2)
		if u6 > 7:
			n9 = 1-n9
			paths.append(3)
		else:
			u6 = u6+n9
			u6 = u6+2
			u6 = 7+8
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