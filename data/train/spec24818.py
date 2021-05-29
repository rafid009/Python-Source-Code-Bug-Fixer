import numpy as np 

def function(x):

	p4 = x
	i0 = 3
	x = 0
	paths = []
	try:
		if x < 0:
			i0 = i0+3
			x = 1+x
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x >= 6:
			i0 = i0+3
			p4 = 9*p4
			paths.append(3)
		else:
			i0 = i0+1
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