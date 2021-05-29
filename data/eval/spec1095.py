import numpy as np 

def function(x):

	y4 = 7
	p6 = 2
	paths = []
	try:
		if x < 7:
			p6 = x*6
			p6 = 3*x
			x = 4+y4
			paths.append(1)
		else:
			p6 = p6-3
			paths.append(2)
		if p6 < 5:
			y4 = p6-y4
			y4 = y4+5
			y4 = y4-4
			paths.append(3)
		else:
			y4 = 2*9
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))