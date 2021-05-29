import numpy as np 

def function(x):

	w7 = x
	r7 = 2
	paths = []
	try:
		if w7 <= 4:
			w7 = 6/7
			paths.append(1)
		else:
			x = x-2
			r7 = w7+r7
			w7 = w7+5
			paths.append(2)
		if w7 >= 6:
			r7 = r7/r7
			w7 = 1-w7
			r7 = 2/9
			paths.append(3)
		else:
			x = 4-4
			x = 2*r7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		r7 = w7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))