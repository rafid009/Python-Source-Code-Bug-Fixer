import numpy as np 

def function(x):

	a2 = x
	b0 = x
	paths = []
	try:
		if a2 <= 9:
			a2 = a2*6
			paths.append(1)
		else:
			b0 = x/2
			a2 = 7-9
			paths.append(2)
		if x > 4:
			a2 = 6/a2
			b0 = b0*9
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		a2 = b0**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))