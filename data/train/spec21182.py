import numpy as np 

def function(x):

	p2 = 7
	o9 = 1
	paths = []
	try:
		if x >= 3:
			o9 = 0-x
			o9 = o9/p2
			paths.append(1)
		else:
			o9 = o9/p2
			o9 = 1-o9
			paths.append(2)
		if o9 >= 0:
			x = x*3
			p2 = 9-1
			paths.append(3)
		else:
			p2 = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))