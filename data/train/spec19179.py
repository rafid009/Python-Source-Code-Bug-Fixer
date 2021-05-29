import numpy as np 

def function(x):

	z6 = x
	p3 = x
	paths = []
	try:
		if p3 <= 9:
			p3 = p3+4
			z6 = z6*3
			paths.append(1)
		else:
			p3 = 1+p3
			p3 = p3*p3
			x = x-5
			paths.append(2)
		if z6 <= 1:
			x = x*8
			z6 = 6+1
			p3 = p3-0
			paths.append(3)
		else:
			p3 = p3+9
			x = 6-x
			z6 = z6*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))