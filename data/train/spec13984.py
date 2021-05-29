import numpy as np 

def function(x):

	y7 = 3
	p4 = x
	paths = []
	try:
		if x >= 8:
			y7 = 3+y7
			p4 = p4-p4
			p4 = 6*p4
			paths.append(1)
		else:
			x = y7/x
			x = x*8
			y7 = y7+2
			paths.append(2)
		if y7 > 3:
			p4 = p4*1
			y7 = y7/x
			x = 9*4
			paths.append(3)
		else:
			y7 = x-3
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))