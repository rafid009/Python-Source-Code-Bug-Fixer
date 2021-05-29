import numpy as np 

def function(x):

	l4 = 8
	x5 = x
	x = 2
	paths = []
	try:
		if x <= 8:
			x = 2*x
			l4 = 0*l4
			l4 = l4*l4
			paths.append(1)
		else:
			x5 = x5*0
			l4 = x-l4
			l4 = l4*6
			paths.append(2)
		if x <= 4:
			x5 = x5-9
			paths.append(3)
		else:
			l4 = l4+0
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))