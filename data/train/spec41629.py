import numpy as np 

def function(x):

	g6 = 3
	o1 = x
	paths = []
	try:
		if o1 > 4:
			x = x*1
			x = 7*x
			paths.append(1)
		else:
			o1 = x*o1
			paths.append(2)
		if x <= 5:
			x = 9+x
			paths.append(3)
		else:
			o1 = 1+o1
			g6 = 1*o1
			x = x*8
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