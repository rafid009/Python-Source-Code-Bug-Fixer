import numpy as np 

def function(x):

	o0 = 1
	w3 = x
	paths = []
	try:
		if x < 9:
			w3 = o0-x
			x = o0+o0
			o0 = 2*2
			paths.append(1)
		else:
			w3 = o0-7
			w3 = o0-w3
			paths.append(2)
		if x >= 8:
			o0 = 7-x
			o0 = o0+0
			w3 = w3*x
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		w3 = o0**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))