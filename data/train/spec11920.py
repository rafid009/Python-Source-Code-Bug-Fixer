import numpy as np 

def function(x):

	x7 = x
	f9 = 4
	paths = []
	try:
		if x < 8:
			x7 = x7*4
			paths.append(1)
		else:
			x = x+4
			x = 6-x
			paths.append(2)
		if x > 7:
			x = x/9
			x = f9-3
			paths.append(3)
		else:
			x = 5*4
			x = 9-1
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))