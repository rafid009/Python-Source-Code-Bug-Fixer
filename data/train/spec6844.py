import numpy as np 

def function(x):

	p8 = x
	y1 = x
	x = x
	paths = []
	try:
		if p8 >= 7:
			x = 4+x
			y1 = 7/y1
			paths.append(1)
		else:
			p8 = y1-2
			p8 = 8-y1
			paths.append(2)
		if p8 <= 1:
			p8 = p8/1
			x = 2-x
			p8 = 3-2
			paths.append(3)
		else:
			p8 = 7+y1
			x = x-8
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		p8 = y1**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))