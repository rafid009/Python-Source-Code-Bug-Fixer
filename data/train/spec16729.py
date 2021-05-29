import numpy as np 

def function(x):

	b4 = x
	x5 = x
	paths = []
	try:
		if x5 <= 4:
			x5 = 8-x5
			paths.append(1)
		else:
			x = 8+x5
			b4 = x/b4
			paths.append(2)
		if b4 > 9:
			x5 = x5-9
			paths.append(3)
		else:
			x = x-8
			x5 = 4-5
			x5 = x5*x5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))