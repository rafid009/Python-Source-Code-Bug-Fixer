import numpy as np 

def function(x):

	h2 = x
	z2 = 4
	paths = []
	try:
		if h2 >= 9:
			h2 = x+z2
			paths.append(1)
		else:
			h2 = h2-4
			z2 = z2+5
			z2 = 5*2
			paths.append(2)
		if z2 >= 4:
			x = 2+3
			x = 3*x
			x = x*4
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))