import numpy as np 

def function(x):

	q8 = 3
	p4 = x
	paths = []
	try:
		if q8 > 5:
			q8 = x+p4
			x = q8-p4
			p4 = p4*q8
			paths.append(1)
		else:
			q8 = 9+2
			p4 = q8-p4
			paths.append(2)
		if p4 > 8:
			q8 = q8-7
			paths.append(3)
		else:
			q8 = q8/2
			x = x*4
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