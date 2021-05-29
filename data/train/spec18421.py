import numpy as np 

def function(x):

	n4 = 9
	o7 = 1
	paths = []
	try:
		if o7 <= 1:
			n4 = 8+4
			o7 = 5*1
			paths.append(1)
		else:
			n4 = 1+5
			paths.append(2)
		if o7 < 2:
			n4 = o7*2
			paths.append(3)
		else:
			n4 = 4+n4
			x = x+5
			n4 = 1-o7
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