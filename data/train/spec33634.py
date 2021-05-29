import numpy as np 

def function(x):

	w3 = x
	o0 = 9
	paths = []
	try:
		if w3 <= 1:
			o0 = o0+x
			paths.append(1)
		else:
			o0 = x*1
			o0 = 6+5
			paths.append(2)
		if o0 < 9:
			w3 = w3-x
			paths.append(3)
		else:
			w3 = w3/o0
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