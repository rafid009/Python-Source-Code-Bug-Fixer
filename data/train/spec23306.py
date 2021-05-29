import numpy as np 

def function(x):

	p7 = x
	p9 = x
	x = 8
	paths = []
	try:
		if x > 6:
			p7 = 6/p7
			paths.append(1)
		else:
			x = 6-4
			paths.append(2)
		if p7 < 0:
			p7 = 0+p9
			p7 = p7/8
			p9 = x+p7
			paths.append(3)
		else:
			p7 = x/4
			x = 0-7
			p7 = 0-x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))