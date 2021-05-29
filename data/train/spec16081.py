import numpy as np 

def function(x):

	b1 = 4
	p6 = x
	paths = []
	try:
		if b1 > 2:
			x = b1*x
			paths.append(1)
		else:
			b1 = 2+1
			p6 = 4/p6
			b1 = b1-8
			paths.append(2)
		if b1 <= 6:
			p6 = 5/p6
			paths.append(3)
		else:
			p6 = 1+p6
			p6 = p6*x
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))