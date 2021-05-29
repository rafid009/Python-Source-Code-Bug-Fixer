import numpy as np 

def function(x):

	p5 = 1
	z1 = 1
	paths = []
	try:
		if p5 <= 6:
			z1 = z1/6
			paths.append(1)
		else:
			z1 = z1-z1
			paths.append(2)
		if z1 <= 7:
			z1 = z1-z1
			p5 = x+1
			p5 = 2-p5
			paths.append(3)
		else:
			z1 = 2/z1
			x = x*6
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		p5 = p5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))