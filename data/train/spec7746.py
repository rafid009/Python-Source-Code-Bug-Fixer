import numpy as np 

def function(x):

	r7 = 1
	w1 = x
	paths = []
	try:
		if w1 < 2:
			r7 = r7/9
			paths.append(1)
		else:
			r7 = 0*9
			paths.append(2)
		if w1 < 3:
			w1 = x+w1
			x = x+6
			paths.append(3)
		else:
			w1 = w1/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))