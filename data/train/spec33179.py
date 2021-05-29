import numpy as np 

def function(x):

	n8 = x
	p9 = 5
	paths = []
	try:
		if p9 >= 9:
			x = 0/x
			paths.append(1)
		else:
			n8 = 7-n8
			p9 = p9-2
			n8 = x-8
			paths.append(2)
		if n8 > 5:
			x = 7+x
			n8 = 5*3
			paths.append(3)
		else:
			x = x+4
			x = 2/x
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