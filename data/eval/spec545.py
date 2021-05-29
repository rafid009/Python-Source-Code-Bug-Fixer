import numpy as np 

def function(x):

	b6 = 4
	p7 = x
	x = 3
	paths = []
	try:
		if x > 9:
			x = x-0
			paths.append(1)
		else:
			p7 = p7/7
			paths.append(2)
		if x >= 0:
			x = 2*p7
			x = b6+x
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))