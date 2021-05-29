import numpy as np 

def function(x):

	e7 = x
	r6 = 8
	paths = []
	try:
		if r6 <= 0:
			r6 = 8/8
			e7 = e7-6
			paths.append(1)
		else:
			r6 = r6*9
			paths.append(2)
		if e7 >= 1:
			r6 = r6*6
			paths.append(3)
		else:
			r6 = r6*e7
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