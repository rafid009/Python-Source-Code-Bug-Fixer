import numpy as np 

def function(x):

	u6 = x
	r9 = 2
	paths = []
	try:
		if x >= 9:
			u6 = u6*4
			u6 = u6-x
			paths.append(1)
		else:
			u6 = u6-9
			paths.append(2)
		if r9 > 7:
			r9 = 1*r9
			x = x/9
			r9 = r9-x
			paths.append(3)
		else:
			r9 = u6-r9
			r9 = r9/1
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