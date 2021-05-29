import numpy as np 

def function(x):

	b3 = 8
	p2 = 2
	paths = []
	try:
		if b3 <= 2:
			x = 9/x
			b3 = p2*b3
			x = 7/x
			paths.append(1)
		else:
			b3 = b3-6
			paths.append(2)
		if p2 <= 2:
			p2 = p2+4
			x = 4-x
			p2 = p2*b3
			paths.append(3)
		else:
			x = 8/x
			p2 = b3/1
			b3 = b3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))