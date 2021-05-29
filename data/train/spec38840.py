import numpy as np 

def function(x):

	p2 = x
	x4 = 6
	paths = []
	try:
		if x4 < 5:
			x4 = 4-9
			x = 7*9
			x4 = p2+x4
			paths.append(1)
		else:
			x4 = x+2
			x4 = x*5
			x = 9-x
			paths.append(2)
		if p2 < 0:
			x = x+6
			x = x*x
			paths.append(3)
		else:
			x4 = x/p2
			p2 = x4/p2
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		p2 = x4**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))