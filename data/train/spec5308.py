import numpy as np 

def function(x):

	l8 = 5
	a2 = x
	paths = []
	try:
		if x <= 8:
			l8 = 3/5
			x = x+x
			paths.append(1)
		else:
			l8 = l8*6
			x = 3*x
			x = l8-x
			paths.append(2)
		if x < 9:
			x = x/2
			a2 = 8-a2
			x = x+l8
			paths.append(3)
		else:
			l8 = 2-9
			x = 7-l8
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))