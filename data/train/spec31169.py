import numpy as np 

def function(x):

	x6 = 5
	b4 = x
	paths = []
	try:
		if b4 < 1:
			b4 = 1/1
			b4 = b4+4
			b4 = x6/6
			paths.append(1)
		else:
			b4 = b4*b4
			paths.append(2)
		if b4 >= 3:
			x = x+b4
			x6 = x6-5
			paths.append(3)
		else:
			x6 = 0-x6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))