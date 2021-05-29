import numpy as np 

def function(x):

	z6 = x
	p6 = x
	paths = []
	try:
		if x <= 3:
			x = z6/x
			p6 = 3/p6
			paths.append(1)
		else:
			p6 = p6+p6
			p6 = p6-0
			paths.append(2)
		if p6 <= 4:
			p6 = z6*4
			z6 = 2/z6
			paths.append(3)
		else:
			x = p6-x
			x = x-1
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		p6 = z6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))