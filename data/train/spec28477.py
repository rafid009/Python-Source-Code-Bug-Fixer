import numpy as np 

def function(x):

	w7 = 4
	r8 = x
	paths = []
	try:
		if x > 8:
			w7 = w7+w7
			x = 7+r8
			paths.append(1)
		else:
			x = 6*x
			w7 = w7-5
			paths.append(2)
		if r8 >= 2:
			w7 = x*x
			r8 = r8*7
			x = 2/4
			paths.append(3)
		else:
			r8 = 6/r8
			r8 = x+r8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))