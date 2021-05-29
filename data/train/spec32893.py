import numpy as np 

def function(x):

	w4 = x
	i6 = 2
	x = x
	paths = []
	try:
		if w4 <= 9:
			x = x+6
			x = x-1
			paths.append(1)
		else:
			i6 = 2-i6
			paths.append(2)
		if i6 < 7:
			w4 = w4-5
			w4 = w4+x
			x = 4-x
			paths.append(3)
		else:
			w4 = w4/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))