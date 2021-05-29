import numpy as np 

def function(x):

	p2 = 5
	y4 = 0
	paths = []
	try:
		if x >= 1:
			x = 2+3
			p2 = p2-7
			p2 = 1/p2
			paths.append(1)
		else:
			y4 = y4-p2
			paths.append(2)
		if p2 <= 0:
			x = 5*x
			paths.append(3)
		else:
			x = 2-x
			x = 6/2
			y4 = x+8
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		y4 = p2**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))