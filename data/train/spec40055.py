import numpy as np 

def function(x):

	w5 = 8
	j4 = 2
	paths = []
	try:
		if w5 < 1:
			x = w5-x
			paths.append(1)
		else:
			x = x-4
			w5 = j4+0
			j4 = 6-j4
			paths.append(2)
		if x <= 9:
			j4 = j4*8
			j4 = 3-x
			paths.append(3)
		else:
			x = 9/4
			w5 = w5-3
			j4 = j4/w5
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