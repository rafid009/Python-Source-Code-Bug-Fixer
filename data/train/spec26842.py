import numpy as np 

def function(x):

	d8 = 3
	u9 = 7
	paths = []
	try:
		if x <= 8:
			d8 = 0*d8
			u9 = 2+u9
			paths.append(1)
		else:
			u9 = 3+5
			u9 = u9-9
			d8 = x+d8
			paths.append(2)
		if d8 < 0:
			x = x+3
			d8 = d8-u9
			paths.append(3)
		else:
			d8 = 7*x
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