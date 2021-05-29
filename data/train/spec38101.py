import numpy as np 

def function(x):

	w6 = 5
	r7 = x
	paths = []
	try:
		if w6 > 2:
			w6 = x-2
			w6 = w6*w6
			paths.append(1)
		else:
			w6 = w6-4
			paths.append(2)
		if r7 > 2:
			w6 = w6-8
			r7 = r7+x
			paths.append(3)
		else:
			r7 = r7/w6
			x = x+x
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