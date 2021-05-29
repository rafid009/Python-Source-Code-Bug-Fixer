import numpy as np 

def function(x):

	x5 = x
	p8 = x
	paths = []
	try:
		if p8 <= 9:
			x = x5+x
			paths.append(1)
		else:
			x = 3/x
			x5 = x5/7
			paths.append(2)
		if x5 <= 9:
			x5 = x5/3
			x5 = x5+0
			paths.append(3)
		else:
			x = p8+x
			x = p8-4
			p8 = p8+8
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))