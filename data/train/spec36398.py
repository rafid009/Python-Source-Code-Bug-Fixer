import numpy as np 

def function(x):

	b6 = x
	x2 = x
	paths = []
	try:
		if x2 <= 2:
			b6 = x2*x
			paths.append(1)
		else:
			x = x+8
			x = x2/5
			paths.append(2)
		if b6 <= 0:
			b6 = x-7
			x = x*9
			paths.append(3)
		else:
			x = x-b6
			b6 = b6/x
			b6 = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))