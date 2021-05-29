import numpy as np 

def function(x):

	w7 = x
	r4 = 1
	paths = []
	try:
		if r4 >= 1:
			w7 = 1-w7
			paths.append(1)
		else:
			w7 = 2+3
			x = r4/x
			r4 = 2-5
			paths.append(2)
		if x >= 9:
			r4 = r4*r4
			paths.append(3)
		else:
			r4 = r4/x
			r4 = r4-r4
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))