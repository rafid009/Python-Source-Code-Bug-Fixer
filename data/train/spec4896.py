import numpy as np 

def function(x):

	p3 = x
	b6 = x
	paths = []
	try:
		if x < 3:
			b6 = 1-2
			paths.append(1)
		else:
			p3 = 2+p3
			paths.append(2)
		if p3 > 7:
			x = x-7
			p3 = 8*p3
			b6 = 1*b6
			paths.append(3)
		else:
			p3 = p3/b6
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