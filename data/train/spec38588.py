import numpy as np 

def function(x):

	w5 = 3
	r8 = 5
	paths = []
	try:
		if w5 > 5:
			x = 5*0
			paths.append(1)
		else:
			w5 = w5*6
			x = x-r8
			paths.append(2)
		if r8 < 5:
			x = 6*x
			w5 = w5*4
			paths.append(3)
		else:
			r8 = r8/4
			w5 = 8-r8
			x = 0-7
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