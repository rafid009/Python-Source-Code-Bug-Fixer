import numpy as np 

def function(x):

	n3 = x
	p9 = x
	paths = []
	try:
		if n3 >= 2:
			x = x-1
			paths.append(1)
		else:
			n3 = 6*n3
			paths.append(2)
		if p9 < 9:
			p9 = p9-6
			n3 = p9*n3
			paths.append(3)
		else:
			n3 = 9-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))