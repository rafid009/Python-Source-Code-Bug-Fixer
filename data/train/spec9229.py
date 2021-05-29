import numpy as np 

def function(x):

	p4 = 7
	n0 = x
	x = 7
	paths = []
	try:
		if n0 <= 4:
			x = 0-8
			p4 = p4*n0
			paths.append(1)
		else:
			n0 = n0-n0
			x = 9/5
			x = x/4
			paths.append(2)
		if p4 < 3:
			p4 = p4-x
			p4 = n0+p4
			x = 6/3
			paths.append(3)
		else:
			n0 = n0+5
			p4 = p4/5
			x = 5+9
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))