import numpy as np 

def function(x):

	x2 = x
	p9 = x
	paths = []
	try:
		if x < 2:
			p9 = p9-x
			x2 = 1+x
			x = x+2
			paths.append(1)
		else:
			x = 0*x
			x2 = 9*3
			paths.append(2)
		if p9 > 2:
			x = p9+3
			x = 1*x
			paths.append(3)
		else:
			x = x-0
			p9 = x*9
			x2 = 2*x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))