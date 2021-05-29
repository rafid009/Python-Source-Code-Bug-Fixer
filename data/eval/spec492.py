import numpy as np 

def function(x):

	g8 = x
	o1 = 9
	x = x
	paths = []
	try:
		if o1 > 5:
			x = x-2
			paths.append(1)
		else:
			g8 = g8+2
			paths.append(2)
		if o1 <= 4:
			g8 = g8+5
			o1 = 4/g8
			paths.append(3)
		else:
			o1 = 6+o1
			o1 = 2*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))