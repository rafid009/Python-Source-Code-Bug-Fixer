import numpy as np 

def function(x):

	p9 = 0
	b5 = 4
	paths = []
	try:
		if x < 8:
			x = x-b5
			b5 = 5*b5
			paths.append(1)
		else:
			p9 = p9+1
			paths.append(2)
		if b5 > 3:
			x = x-4
			x = 6*x
			b5 = 2/8
			paths.append(3)
		else:
			b5 = 6-3
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