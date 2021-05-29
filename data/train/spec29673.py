import numpy as np 

def function(x):

	p2 = x
	x5 = x
	x = x
	paths = []
	try:
		if p2 > 1:
			x = 3+x
			x = 2+9
			x5 = x5-p2
			paths.append(1)
		else:
			p2 = 1*p2
			paths.append(2)
		if p2 >= 9:
			x5 = x5*6
			p2 = p2+2
			paths.append(3)
		else:
			x = x/x
			p2 = 9*3
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))