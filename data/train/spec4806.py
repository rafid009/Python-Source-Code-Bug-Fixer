import numpy as np 

def function(x):

	p4 = x
	h7 = 8
	paths = []
	try:
		if p4 < 2:
			p4 = p4-5
			x = h7*2
			paths.append(1)
		else:
			h7 = h7/p4
			paths.append(2)
		if p4 > 1:
			h7 = h7+x
			paths.append(3)
		else:
			h7 = h7-h7
			h7 = p4-4
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