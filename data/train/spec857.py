import numpy as np 

def function(x):

	y4 = x
	p4 = 9
	paths = []
	try:
		if p4 < 1:
			y4 = 1-8
			x = y4*3
			y4 = y4+7
			paths.append(1)
		else:
			p4 = p4+7
			p4 = p4-7
			paths.append(2)
		if x > 2:
			x = x+2
			p4 = p4-5
			p4 = p4+1
			paths.append(3)
		else:
			y4 = 9*y4
			x = x-p4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		p4 = y4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))