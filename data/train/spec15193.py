import numpy as np 

def function(x):

	p1 = 6
	y1 = x
	paths = []
	try:
		if x >= 9:
			p1 = p1*5
			paths.append(1)
		else:
			p1 = x*4
			p1 = 0/p1
			p1 = p1/x
			paths.append(2)
		if y1 <= 3:
			p1 = y1*p1
			p1 = y1*4
			y1 = p1*5
			paths.append(3)
		else:
			x = x*8
			x = 1/7
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))