import numpy as np 

def function(x):

	o5 = 6
	g1 = x
	paths = []
	try:
		if g1 >= 0:
			x = x-o5
			x = x*8
			paths.append(1)
		else:
			g1 = x/4
			paths.append(2)
		if o5 > 7:
			g1 = o5+0
			paths.append(3)
		else:
			g1 = 7/g1
			g1 = g1*g1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))