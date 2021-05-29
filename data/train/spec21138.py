import numpy as np 

def function(x):

	x0 = x
	p9 = 9
	paths = []
	try:
		if x > 1:
			x0 = 0/x0
			x = 7/x
			paths.append(1)
		else:
			p9 = x0+x
			x = 7+x
			paths.append(2)
		if x >= 2:
			p9 = 3*p9
			x = p9/4
			paths.append(3)
		else:
			p9 = p9+7
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		p9 = x0**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))