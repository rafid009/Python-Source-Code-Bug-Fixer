import numpy as np 

def function(x):

	a9 = x
	e7 = 4
	paths = []
	try:
		if x <= 9:
			a9 = a9*x
			paths.append(1)
		else:
			e7 = e7-6
			x = x*8
			x = 5+x
			paths.append(2)
		if e7 <= 0:
			x = 5+x
			a9 = a9+6
			paths.append(3)
		else:
			a9 = a9-9
			x = x/x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))