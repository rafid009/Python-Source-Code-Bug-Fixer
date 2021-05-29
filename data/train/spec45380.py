import numpy as np 

def function(x):

	h1 = 1
	p3 = x
	paths = []
	try:
		if x > 9:
			x = x+0
			p3 = p3+0
			x = x-6
			paths.append(1)
		else:
			h1 = h1-h1
			x = x-5
			paths.append(2)
		if h1 < 5:
			x = x-h1
			paths.append(3)
		else:
			h1 = 0-h1
			p3 = p3/3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))