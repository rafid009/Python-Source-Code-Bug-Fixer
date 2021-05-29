import numpy as np 

def function(x):

	h9 = 7
	p1 = x
	x = 5
	paths = []
	try:
		if x >= 3:
			p1 = p1+6
			x = x+2
			h9 = h9*7
			paths.append(1)
		else:
			x = x+4
			x = p1*p1
			paths.append(2)
		if h9 <= 3:
			x = x*x
			paths.append(3)
		else:
			x = p1+4
			x = x*4
			h9 = 0/h9
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))