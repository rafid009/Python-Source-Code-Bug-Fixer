import numpy as np 

def function(x):

	p2 = 7
	b9 = 6
	paths = []
	try:
		if b9 < 3:
			p2 = 4*p2
			p2 = p2*b9
			x = x/p2
			paths.append(1)
		else:
			b9 = b9-2
			b9 = 8-b9
			p2 = 7+x
			paths.append(2)
		if b9 >= 3:
			b9 = 0-9
			b9 = b9/4
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))