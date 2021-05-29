import numpy as np 

def function(x):

	t1 = 1
	b9 = x
	paths = []
	try:
		if x < 5:
			b9 = b9*2
			paths.append(1)
		else:
			b9 = 9-x
			b9 = 9*b9
			b9 = b9*4
			paths.append(2)
		if b9 > 1:
			b9 = 7+b9
			paths.append(3)
		else:
			x = 2*x
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