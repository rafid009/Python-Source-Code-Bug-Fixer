import numpy as np 

def function(x):

	n0 = 9
	p4 = 2
	paths = []
	try:
		if n0 >= 7:
			n0 = 6/n0
			x = x/1
			paths.append(1)
		else:
			p4 = p4/8
			n0 = x-p4
			paths.append(2)
		if p4 > 9:
			n0 = p4/5
			x = 7/4
			paths.append(3)
		else:
			n0 = n0/x
			p4 = p4-x
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		n0 = p4**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))