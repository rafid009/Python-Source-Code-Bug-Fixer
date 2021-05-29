import numpy as np 

def function(x):

	b3 = 6
	x2 = x
	x = x
	paths = []
	try:
		if b3 <= 6:
			b3 = x2+9
			x = x+8
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if b3 >= 4:
			x = x2/8
			paths.append(3)
		else:
			x = 5*x2
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