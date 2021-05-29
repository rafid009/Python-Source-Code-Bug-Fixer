import numpy as np 

def function(x):

	r4 = x
	w7 = 1
	paths = []
	try:
		if x < 7:
			r4 = r4-w7
			w7 = r4+w7
			paths.append(1)
		else:
			x = x+x
			w7 = 7*w7
			x = x-6
			paths.append(2)
		if w7 <= 3:
			r4 = x*6
			x = 1/x
			x = 7+r4
			paths.append(3)
		else:
			w7 = w7-r4
			r4 = r4*r4
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