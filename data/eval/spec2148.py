import numpy as np 

def function(x):

	p9 = x
	z1 = x
	paths = []
	try:
		if x < 3:
			p9 = z1*2
			p9 = p9-p9
			paths.append(1)
		else:
			p9 = p9-p9
			p9 = 9/2
			x = 9/9
			paths.append(2)
		if x > 4:
			p9 = p9/4
			paths.append(3)
		else:
			z1 = z1/6
			z1 = z1/1
			p9 = z1/9
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