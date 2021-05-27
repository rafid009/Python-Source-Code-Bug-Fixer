import numpy as np 

def function(x):

	h5 = 1
	p4 = x
	paths = []
	try:
		if h5 < 3:
			h5 = h5+x
			p4 = p4+h5
			x = 1+6
			paths.append(1)
		else:
			p4 = x/9
			paths.append(2)
		if p4 >= 4:
			h5 = x-9
			p4 = p4-h5
			paths.append(3)
		else:
			x = x/p4
			p4 = 8*p4
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))