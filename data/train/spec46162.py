import numpy as np 

def function(x):

	n8 = x
	u6 = 0
	paths = []
	try:
		if u6 <= 4:
			u6 = u6-6
			paths.append(1)
		else:
			n8 = n8+7
			u6 = u6*u6
			paths.append(2)
		if n8 < 4:
			u6 = u6-1
			paths.append(3)
		else:
			x = 5*n8
			n8 = n8*x
			n8 = n8*3
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