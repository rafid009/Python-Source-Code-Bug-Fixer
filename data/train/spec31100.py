import numpy as np 

def function(x):

	x8 = x
	p7 = x
	paths = []
	try:
		if p7 <= 3:
			x8 = 7+x8
			paths.append(1)
		else:
			p7 = 6+p7
			paths.append(2)
		if x > 0:
			x = x/4
			x = 8-x
			paths.append(3)
		else:
			x = x*p7
			p7 = x/p7
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