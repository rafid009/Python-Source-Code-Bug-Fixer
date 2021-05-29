import numpy as np 

def function(x):

	o0 = 4
	n6 = 2
	paths = []
	try:
		if x < 7:
			n6 = n6-6
			paths.append(1)
		else:
			o0 = 2*0
			paths.append(2)
		if o0 < 0:
			x = n6*n6
			o0 = o0+o0
			paths.append(3)
		else:
			o0 = x+o0
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