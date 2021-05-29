import numpy as np 

def function(x):

	p4 = x
	p3 = 6
	paths = []
	try:
		if x >= 7:
			p3 = p4/p3
			p3 = x/1
			paths.append(1)
		else:
			x = 9/1
			paths.append(2)
		if p4 < 1:
			x = p3/8
			x = x/4
			paths.append(3)
		else:
			p4 = p4*4
			x = 4*x
			p4 = p4*1
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p3 = p4**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))