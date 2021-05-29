import numpy as np 

def function(x):

	i8 = 9
	w8 = x
	paths = []
	try:
		if w8 > 5:
			x = 0*w8
			paths.append(1)
		else:
			x = x-9
			i8 = 5*i8
			w8 = 8*x
			paths.append(2)
		if w8 < 5:
			i8 = x/2
			x = x/5
			paths.append(3)
		else:
			x = x/4
			i8 = i8/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))