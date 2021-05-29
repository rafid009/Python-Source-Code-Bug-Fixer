import numpy as np 

def function(x):

	p4 = x
	y0 = 1
	paths = []
	try:
		if y0 >= 1:
			x = x-4
			x = x-8
			y0 = p4/6
			paths.append(1)
		else:
			p4 = p4/5
			x = p4+7
			p4 = p4+1
			paths.append(2)
		if y0 >= 9:
			p4 = p4/7
			paths.append(3)
		else:
			p4 = y0+p4
			p4 = 9/1
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		p4 = y0**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))