import numpy as np 

def function(x):

	p8 = x
	b0 = 9
	paths = []
	try:
		if x >= 1:
			x = x*b0
			b0 = 8+b0
			p8 = 4/p8
			paths.append(1)
		else:
			x = x*p8
			b0 = p8-3
			x = x+4
			paths.append(2)
		if x < 1:
			p8 = 4/7
			b0 = x/b0
			paths.append(3)
		else:
			x = x-p8
			b0 = 0/p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))