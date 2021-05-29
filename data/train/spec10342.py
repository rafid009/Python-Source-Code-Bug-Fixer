import numpy as np 

def function(x):

	w4 = x
	k7 = 1
	x = 6
	paths = []
	try:
		if k7 >= 8:
			w4 = w4-9
			paths.append(1)
		else:
			w4 = w4*8
			k7 = w4*k7
			paths.append(2)
		if k7 <= 4:
			x = x/4
			x = w4*9
			paths.append(3)
		else:
			k7 = w4+w4
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))