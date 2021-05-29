import numpy as np 

def function(x):

	p4 = 9
	h2 = 2
	paths = []
	try:
		if h2 < 4:
			p4 = p4-p4
			h2 = 9-x
			x = 2/x
			paths.append(1)
		else:
			h2 = h2*3
			paths.append(2)
		if p4 > 1:
			h2 = p4-h2
			h2 = h2+6
			paths.append(3)
		else:
			h2 = h2*3
			x = 7*p4
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		p4 = h2**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))