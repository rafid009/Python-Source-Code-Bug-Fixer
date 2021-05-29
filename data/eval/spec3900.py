import numpy as np 

def function(x):

	o6 = 8
	g3 = 4
	paths = []
	try:
		if o6 >= 5:
			g3 = 5*g3
			x = o6/x
			g3 = 1-x
			paths.append(1)
		else:
			g3 = o6/4
			g3 = g3*9
			paths.append(2)
		if o6 > 2:
			g3 = 4+x
			x = x-9
			g3 = g3+9
			paths.append(3)
		else:
			x = 4*9
			g3 = 2+1
			g3 = g3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))