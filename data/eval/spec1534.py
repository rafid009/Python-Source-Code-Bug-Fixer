import numpy as np 

def function(x):

	j8 = 6
	w8 = 7
	paths = []
	try:
		if x <= 5:
			x = 2-x
			paths.append(1)
		else:
			x = 2/7
			w8 = w8-2
			w8 = x+6
			paths.append(2)
		if w8 < 8:
			j8 = x-9
			x = 1+j8
			paths.append(3)
		else:
			j8 = 6*j8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))