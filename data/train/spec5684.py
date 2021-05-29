import numpy as np 

def function(x):

	o0 = 1
	w3 = 6
	x = x
	paths = []
	try:
		if x > 8:
			w3 = 8/4
			x = x/w3
			w3 = o0-0
			paths.append(1)
		else:
			w3 = w3+x
			paths.append(2)
		if x < 6:
			w3 = 3-w3
			o0 = o0-x
			w3 = 5/3
			paths.append(3)
		else:
			o0 = 6-x
			o0 = o0*o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))