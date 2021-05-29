import numpy as np 

def function(x):

	w2 = x
	v0 = 2
	paths = []
	try:
		if w2 < 2:
			x = w2/8
			paths.append(1)
		else:
			v0 = v0/3
			paths.append(2)
		if w2 <= 6:
			v0 = v0*8
			v0 = 0+3
			paths.append(3)
		else:
			v0 = v0/3
			w2 = w2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))