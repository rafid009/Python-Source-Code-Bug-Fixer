import numpy as np 

def function(x):

	o5 = 9
	x2 = x
	paths = []
	try:
		if x >= 3:
			o5 = o5*1
			paths.append(1)
		else:
			o5 = 4+1
			o5 = 1+o5
			paths.append(2)
		if o5 < 1:
			o5 = 4+o5
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))