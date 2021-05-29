import numpy as np 

def function(x):

	z4 = 9
	p4 = x
	paths = []
	try:
		if p4 < 6:
			x = x-p4
			paths.append(1)
		else:
			p4 = 7+z4
			z4 = 0+z4
			p4 = x-9
			paths.append(2)
		if p4 >= 7:
			x = x*6
			p4 = p4+p4
			paths.append(3)
		else:
			z4 = z4*z4
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))