import numpy as np 

def function(x):

	a2 = 1
	x9 = 3
	paths = []
	try:
		if x9 > 6:
			a2 = 5-a2
			paths.append(1)
		else:
			x = 8*x
			x9 = 0-3
			x = 1/3
			paths.append(2)
		if x9 >= 1:
			x = x-a2
			x = a2+3
			paths.append(3)
		else:
			x = x*8
			a2 = a2*a2
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))