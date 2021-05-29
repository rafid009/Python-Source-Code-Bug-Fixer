import numpy as np 

def function(x):

	b0 = 4
	z5 = x
	paths = []
	try:
		if x <= 4:
			b0 = 7-b0
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if b0 < 0:
			x = 1/3
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))