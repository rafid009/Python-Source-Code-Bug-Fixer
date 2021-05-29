import numpy as np 

def function(x):

	r1 = x
	h4 = x
	paths = []
	try:
		if h4 < 6:
			r1 = 4/r1
			paths.append(1)
		else:
			x = 7+5
			r1 = r1+8
			paths.append(2)
		if r1 >= 1:
			x = x+9
			x = x/5
			paths.append(3)
		else:
			r1 = 1+h4
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