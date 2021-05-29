import numpy as np 

def function(x):

	x9 = 1
	r2 = 3
	paths = []
	try:
		if r2 <= 6:
			x = x-x9
			paths.append(1)
		else:
			x9 = x9-9
			paths.append(2)
		if x > 0:
			x = x*8
			x = x9-9
			paths.append(3)
		else:
			x9 = x+x9
			x9 = x9/x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))