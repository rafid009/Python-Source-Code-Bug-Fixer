import numpy as np 

def function(x):

	b4 = x
	a9 = x
	paths = []
	try:
		if a9 >= 7:
			b4 = 3+b4
			paths.append(1)
		else:
			x = 2*a9
			x = 3/x
			x = a9+x
			paths.append(2)
		if x >= 7:
			x = 9-b4
			a9 = a9*a9
			paths.append(3)
		else:
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		b4 = a9**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))