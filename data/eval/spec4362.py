import numpy as np 

def function(x):

	l8 = x
	p7 = 8
	paths = []
	try:
		if p7 > 3:
			x = 3-9
			paths.append(1)
		else:
			l8 = l8+0
			p7 = x-p7
			x = x-2
			paths.append(2)
		if l8 < 2:
			x = 0-8
			p7 = p7+8
			paths.append(3)
		else:
			l8 = l8+6
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))