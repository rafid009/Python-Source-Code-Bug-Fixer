import numpy as np 

def function(x):

	b9 = x
	p3 = x
	paths = []
	try:
		if x > 2:
			b9 = 4*x
			p3 = x/7
			paths.append(1)
		else:
			b9 = x+x
			b9 = 8-b9
			b9 = b9-b9
			paths.append(2)
		if b9 <= 0:
			b9 = b9*6
			p3 = x+p3
			paths.append(3)
		else:
			p3 = 4*b9
			b9 = 0*p3
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