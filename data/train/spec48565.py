import numpy as np 

def function(x):

	p2 = x
	z7 = 8
	paths = []
	try:
		if p2 <= 8:
			z7 = z7/3
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if z7 <= 1:
			p2 = p2+p2
			p2 = 2-p2
			paths.append(3)
		else:
			p2 = 1-8
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))