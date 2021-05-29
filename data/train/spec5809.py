import numpy as np 

def function(x):

	w7 = x
	r6 = x
	paths = []
	try:
		if r6 >= 9:
			w7 = 1+4
			paths.append(1)
		else:
			w7 = 3/4
			x = x+2
			paths.append(2)
		if r6 > 5:
			x = x*4
			r6 = 2*r6
			paths.append(3)
		else:
			r6 = 1*r6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))