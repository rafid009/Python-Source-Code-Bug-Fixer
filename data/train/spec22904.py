import numpy as np 

def function(x):

	b1 = 4
	p7 = 5
	paths = []
	try:
		if p7 <= 6:
			b1 = 9+b1
			p7 = p7*b1
			paths.append(1)
		else:
			x = 5*8
			paths.append(2)
		if x <= 8:
			p7 = p7/p7
			p7 = 4/p7
			paths.append(3)
		else:
			x = x-p7
			p7 = 4+x
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