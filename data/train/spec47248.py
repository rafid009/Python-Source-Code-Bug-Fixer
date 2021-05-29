import numpy as np 

def function(x):

	p1 = 5
	z9 = x
	paths = []
	try:
		if p1 <= 0:
			p1 = 1-p1
			paths.append(1)
		else:
			z9 = z9-3
			z9 = 6/z9
			p1 = p1*x
			paths.append(2)
		if z9 < 7:
			x = 9/z9
			z9 = 6-2
			paths.append(3)
		else:
			x = p1/5
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))