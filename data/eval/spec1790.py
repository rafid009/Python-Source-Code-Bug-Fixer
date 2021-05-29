import numpy as np 

def function(x):

	r9 = x
	j8 = 6
	paths = []
	try:
		if x > 0:
			r9 = 4-r9
			paths.append(1)
		else:
			j8 = j8+4
			j8 = 3*j8
			paths.append(2)
		if x <= 5:
			x = x*9
			paths.append(3)
		else:
			x = x+6
			j8 = x-0
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