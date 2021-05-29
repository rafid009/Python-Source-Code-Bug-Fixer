import numpy as np 

def function(x):

	p3 = 7
	y2 = 8
	x = x
	paths = []
	try:
		if y2 > 2:
			x = 2*x
			p3 = p3*9
			y2 = y2-2
			paths.append(1)
		else:
			p3 = 4-p3
			p3 = 9+p3
			y2 = x-y2
			paths.append(2)
		if p3 >= 0:
			y2 = x+y2
			p3 = 5+p3
			x = p3/x
			paths.append(3)
		else:
			p3 = p3-p3
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		p3 = y2**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))