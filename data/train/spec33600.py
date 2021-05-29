import numpy as np 

def function(x):

	p8 = x
	x0 = x
	paths = []
	try:
		if x < 2:
			x = x/9
			p8 = p8+5
			x = x*4
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if x0 <= 5:
			p8 = p8/2
			p8 = p8*4
			paths.append(3)
		else:
			x0 = 3/6
			p8 = 2-x0
			x0 = p8-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))