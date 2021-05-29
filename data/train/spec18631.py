import numpy as np 

def function(x):

	p7 = 9
	z8 = 9
	paths = []
	try:
		if p7 <= 9:
			x = x+2
			x = 5*x
			p7 = 6/p7
			paths.append(1)
		else:
			x = x/6
			z8 = x-z8
			p7 = 7+p7
			paths.append(2)
		if z8 >= 3:
			z8 = z8+x
			p7 = p7*6
			p7 = p7/1
			paths.append(3)
		else:
			p7 = x-p7
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		p7 = z8**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))