import numpy as np 

def function(x):

	x5 = x
	b6 = x
	paths = []
	try:
		if x <= 0:
			x = 0/x
			paths.append(1)
		else:
			x5 = 4*x5
			b6 = 9*b6
			b6 = b6-4
			paths.append(2)
		if b6 <= 1:
			x = 9+9
			x = b6*3
			x = x*x
			paths.append(3)
		else:
			x5 = x5*5
			x5 = x5-5
			b6 = 5*9
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))