import numpy as np 

def function(x):

	r1 = 6
	w7 = 8
	paths = []
	try:
		if w7 > 4:
			r1 = r1+7
			paths.append(1)
		else:
			x = 4-x
			w7 = w7+3
			paths.append(2)
		if x < 0:
			w7 = w7/w7
			w7 = 2*w7
			r1 = r1+6
			paths.append(3)
		else:
			r1 = 6*r1
			r1 = r1/7
			w7 = 9/w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))