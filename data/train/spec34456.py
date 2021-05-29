import numpy as np 

def function(x):

	g0 = 2
	o1 = x
	paths = []
	try:
		if o1 > 3:
			x = x-x
			paths.append(1)
		else:
			o1 = 4+o1
			x = 4/x
			paths.append(2)
		if o1 < 9:
			x = x*x
			x = o1*x
			g0 = 8/g0
			paths.append(3)
		else:
			g0 = 3+g0
			x = x+o1
			o1 = 5/x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))