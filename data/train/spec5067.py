import numpy as np 

def function(x):

	p4 = x
	b7 = x
	paths = []
	try:
		if x > 6:
			b7 = p4*b7
			p4 = p4*9
			p4 = 1/2
			paths.append(1)
		else:
			p4 = 0+b7
			paths.append(2)
		if x >= 8:
			x = 4/x
			paths.append(3)
		else:
			b7 = p4*p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		b7 = p4**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))