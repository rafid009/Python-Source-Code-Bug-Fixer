import numpy as np 

def function(x):

	z9 = 1
	p4 = x
	paths = []
	try:
		if z9 > 2:
			p4 = 1+p4
			z9 = z9-p4
			paths.append(1)
		else:
			p4 = x+x
			x = x+0
			paths.append(2)
		if x < 7:
			x = 0*5
			paths.append(3)
		else:
			z9 = z9*6
			x = x+1
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))