import numpy as np 

def function(x):

	c8 = 6
	b2 = 5
	paths = []
	try:
		if c8 < 3:
			b2 = b2*b2
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if c8 <= 4:
			x = x*0
			b2 = 1*b2
			paths.append(3)
		else:
			x = x/b2
			b2 = b2-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))