import numpy as np 

def function(x):

	r5 = 7
	e3 = 7
	paths = []
	try:
		if x < 1:
			r5 = r5+r5
			r5 = 3+r5
			paths.append(1)
		else:
			x = 2-r5
			paths.append(2)
		if x < 7:
			e3 = x/1
			r5 = 3+8
			r5 = r5+2
			paths.append(3)
		else:
			x = e3-x
			r5 = r5*7
			e3 = e3*1
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