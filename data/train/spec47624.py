import numpy as np 

def function(x):

	b1 = x
	b8 = x
	paths = []
	try:
		if b1 < 8:
			b1 = 6/b1
			x = x*5
			paths.append(1)
		else:
			b8 = b8*b1
			paths.append(2)
		if x < 2:
			b1 = 3*b1
			paths.append(3)
		else:
			x = x-7
			b1 = b1*9
			x = x*0
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