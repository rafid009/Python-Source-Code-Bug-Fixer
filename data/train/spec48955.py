import numpy as np 

def function(x):

	a9 = x
	p4 = x
	x = 1
	paths = []
	try:
		if a9 >= 9:
			a9 = 5+p4
			a9 = 4*p4
			paths.append(1)
		else:
			a9 = p4+a9
			a9 = 5+6
			paths.append(2)
		if x >= 3:
			p4 = p4+2
			p4 = p4/3
			paths.append(3)
		else:
			a9 = x+0
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))