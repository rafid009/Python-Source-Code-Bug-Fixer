import numpy as np 

def function(x):

	w3 = x
	o0 = 9
	paths = []
	try:
		if o0 >= 2:
			x = 6*w3
			paths.append(1)
		else:
			x = 1-x
			o0 = o0-9
			o0 = o0-w3
			paths.append(2)
		if x < 9:
			o0 = o0/2
			paths.append(3)
		else:
			o0 = w3/6
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		o0 = w3**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))