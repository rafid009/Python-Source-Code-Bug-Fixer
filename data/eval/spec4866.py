import numpy as np 

def function(x):

	p6 = 1
	n4 = x
	x = x
	paths = []
	try:
		if p6 <= 0:
			p6 = x-p6
			p6 = 5-2
			x = 4-x
			paths.append(1)
		else:
			n4 = n4*p6
			n4 = 5*n4
			paths.append(2)
		if x < 8:
			p6 = p6-7
			x = 5-7
			paths.append(3)
		else:
			p6 = 7/x
			x = x+9
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		p6 = n4**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))