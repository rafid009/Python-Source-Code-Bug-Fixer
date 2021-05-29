import numpy as np 

def function(x):

	p2 = 5
	z9 = x
	paths = []
	try:
		if x <= 0:
			p2 = p2/p2
			z9 = z9/3
			z9 = z9-8
			paths.append(1)
		else:
			p2 = x+7
			paths.append(2)
		if z9 <= 0:
			x = x-p2
			paths.append(3)
		else:
			z9 = 9/3
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		p2 = z9**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))