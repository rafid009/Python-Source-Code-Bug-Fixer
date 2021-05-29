import numpy as np 

def function(x):

	b3 = x
	a4 = x
	x = 8
	paths = []
	try:
		if a4 <= 4:
			x = x/b3
			paths.append(1)
		else:
			a4 = 5*a4
			x = 8*a4
			a4 = 0-a4
			paths.append(2)
		if x <= 9:
			x = x*4
			paths.append(3)
		else:
			x = 9/x
			x = x/8
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))