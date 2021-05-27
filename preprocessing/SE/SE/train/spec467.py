import numpy as np 

def function(x):

	h8 = x
	w1 = 4
	paths = []
	try:
		if w1 >= 4:
			x = 7*x
			paths.append(1)
		else:
			x = 1+4
			paths.append(2)
		if x <= 5:
			x = x+0
			w1 = 1-0
			x = 6/x
			paths.append(3)
		else:
			w1 = w1/6
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))