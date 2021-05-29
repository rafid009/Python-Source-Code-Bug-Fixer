import numpy as np 

def function(x):

	b7 = 6
	p3 = x
	paths = []
	try:
		if p3 > 4:
			x = 6/x
			paths.append(1)
		else:
			p3 = p3*x
			x = x*3
			b7 = p3+b7
			paths.append(2)
		if p3 > 6:
			p3 = p3/6
			paths.append(3)
		else:
			p3 = 2-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))