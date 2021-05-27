import numpy as np 

def function(x):

	o0 = 0
	n6 = x
	paths = []
	try:
		if n6 <= 6:
			x = 4+x
			paths.append(1)
		else:
			n6 = n6+5
			x = n6+x
			o0 = 9*n6
			paths.append(2)
		if x <= 4:
			x = x/9
			x = x/9
			paths.append(3)
		else:
			n6 = n6/x
			x = o0+3
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