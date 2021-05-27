import numpy as np 

def function(x):

	w4 = x
	h2 = x
	paths = []
	try:
		if w4 <= 1:
			h2 = h2+h2
			x = 4*x
			paths.append(1)
		else:
			w4 = w4*1
			paths.append(2)
		if w4 <= 9:
			h2 = h2/8
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))