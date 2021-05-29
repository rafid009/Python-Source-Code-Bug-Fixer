import numpy as np 

def function(x):

	r9 = 9
	n6 = x
	paths = []
	try:
		if r9 > 8:
			n6 = n6*r9
			paths.append(1)
		else:
			x = 9/x
			r9 = 0+r9
			paths.append(2)
		if r9 < 9:
			x = 4-x
			paths.append(3)
		else:
			r9 = n6*9
			n6 = n6*1
			r9 = r9/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))