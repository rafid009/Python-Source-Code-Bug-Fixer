import numpy as np 

def function(x):

	x5 = 4
	x9 = 5
	paths = []
	try:
		if x5 >= 1:
			x9 = x9*8
			x9 = x9/2
			paths.append(1)
		else:
			x5 = 3*0
			x9 = 2/x9
			x5 = x5/x
			paths.append(2)
		if x9 <= 3:
			x9 = 2+x9
			x9 = x9+0
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))