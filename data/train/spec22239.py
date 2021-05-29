import numpy as np 

def function(x):

	b4 = x
	b0 = x
	paths = []
	try:
		if b0 >= 4:
			b4 = b4/x
			paths.append(1)
		else:
			x = 7*x
			b0 = 5-b0
			x = x/4
			paths.append(2)
		if b4 <= 3:
			b0 = b0-5
			b0 = x-b0
			x = 9+x
			paths.append(3)
		else:
			x = x/x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))