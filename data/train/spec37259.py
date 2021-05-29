import numpy as np 

def function(x):

	p4 = x
	h2 = 9
	x = 5
	paths = []
	try:
		if p4 > 2:
			h2 = 3-h2
			paths.append(1)
		else:
			p4 = 0+p4
			p4 = 1/2
			paths.append(2)
		if x <= 2:
			p4 = 7-1
			h2 = 7+3
			p4 = 2/5
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))