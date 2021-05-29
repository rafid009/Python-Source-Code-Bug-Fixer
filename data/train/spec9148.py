import numpy as np 

def function(x):

	y5 = 9
	p1 = 3
	paths = []
	try:
		if p1 > 8:
			y5 = 6/3
			y5 = y5*8
			paths.append(1)
		else:
			y5 = y5+p1
			p1 = 1+p1
			y5 = y5+8
			paths.append(2)
		if x > 5:
			x = x/8
			y5 = 0-p1
			paths.append(3)
		else:
			x = p1/3
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))