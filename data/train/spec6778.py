import numpy as np 

def function(x):

	p7 = 7
	y1 = x
	paths = []
	try:
		if y1 <= 1:
			p7 = x*8
			y1 = 6/x
			x = 9/p7
			paths.append(1)
		else:
			p7 = 6-p7
			p7 = p7/y1
			x = x+x
			paths.append(2)
		if p7 >= 8:
			y1 = x*y1
			y1 = y1-p7
			paths.append(3)
		else:
			p7 = 7/x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		p7 = y1**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))