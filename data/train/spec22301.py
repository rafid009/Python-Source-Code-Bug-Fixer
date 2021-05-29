import numpy as np 

def function(x):

	b2 = x
	b3 = 0
	x = x
	paths = []
	try:
		if b3 < 2:
			b2 = 6/x
			b2 = 4+b2
			b2 = b2+5
			paths.append(1)
		else:
			b2 = b2*4
			b3 = b3/b2
			x = x*x
			paths.append(2)
		if x > 3:
			x = x/4
			paths.append(3)
		else:
			b2 = b2/3
			b2 = 3/2
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