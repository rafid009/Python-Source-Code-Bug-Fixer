import numpy as np 

def function(x):

	n4 = 3
	p9 = x
	paths = []
	try:
		if n4 > 6:
			x = x+n4
			x = n4-x
			x = n4/5
			paths.append(1)
		else:
			p9 = p9*6
			paths.append(2)
		if p9 > 3:
			x = x+8
			x = 6/7
			paths.append(3)
		else:
			n4 = 3/n4
			n4 = n4-8
			p9 = 1/n4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))