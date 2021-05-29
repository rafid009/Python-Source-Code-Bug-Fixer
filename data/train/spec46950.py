import numpy as np 

def function(x):

	x2 = x
	o0 = 9
	paths = []
	try:
		if x2 > 2:
			x = x/x2
			o0 = x2+3
			paths.append(1)
		else:
			x2 = 4+o0
			paths.append(2)
		if x2 <= 6:
			x = 2*4
			x2 = 3-x2
			x2 = x2-9
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))