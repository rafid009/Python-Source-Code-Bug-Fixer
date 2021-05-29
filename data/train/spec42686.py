import numpy as np 

def function(x):

	d9 = 6
	p2 = x
	paths = []
	try:
		if x <= 9:
			p2 = 0+p2
			p2 = p2-9
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if x > 1:
			p2 = 0-p2
			x = x/7
			paths.append(3)
		else:
			x = 7*x
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