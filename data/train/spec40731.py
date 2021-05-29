import numpy as np 

def function(x):

	h3 = 4
	b1 = 2
	paths = []
	try:
		if b1 <= 0:
			x = 8-x
			b1 = b1*0
			paths.append(1)
		else:
			x = x*4
			b1 = b1*x
			h3 = h3*h3
			paths.append(2)
		if b1 <= 8:
			x = x-6
			paths.append(3)
		else:
			x = h3/7
			b1 = h3+0
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