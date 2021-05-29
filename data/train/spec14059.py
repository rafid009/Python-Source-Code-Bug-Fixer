import numpy as np 

def function(x):

	y8 = 6
	p2 = x
	x = x
	paths = []
	try:
		if y8 >= 7:
			y8 = 0+x
			x = 1*x
			paths.append(1)
		else:
			p2 = 5+p2
			paths.append(2)
		if x >= 3:
			x = x*x
			p2 = 3+p2
			paths.append(3)
		else:
			y8 = x/y8
			x = 0+x
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		p2 = y8**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))