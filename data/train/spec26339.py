import numpy as np 

def function(x):

	w5 = 0
	i4 = x
	paths = []
	try:
		if x < 6:
			i4 = w5*i4
			paths.append(1)
		else:
			w5 = 0-2
			x = w5-x
			i4 = i4*i4
			paths.append(2)
		if w5 < 8:
			i4 = 1*x
			paths.append(3)
		else:
			i4 = 9*i4
			x = i4-x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))