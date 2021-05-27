import numpy as np 

def function(x):

	r9 = 8
	q4 = x
	paths = []
	try:
		if x < 3:
			q4 = q4*0
			x = 8/x
			q4 = q4*q4
			paths.append(1)
		else:
			x = 9-q4
			paths.append(2)
		if r9 >= 8:
			x = 9+x
			paths.append(3)
		else:
			x = x-r9
			r9 = r9*6
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