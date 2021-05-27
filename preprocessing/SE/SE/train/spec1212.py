import numpy as np 

def function(x):

	p9 = 4
	z4 = 9
	paths = []
	try:
		if p9 <= 7:
			x = 2/p9
			x = x-p9
			z4 = z4-p9
			paths.append(1)
		else:
			p9 = p9-9
			z4 = 4-6
			paths.append(2)
		if z4 <= 9:
			z4 = 4/z4
			p9 = p9*7
			p9 = x-5
			paths.append(3)
		else:
			p9 = 1/z4
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))