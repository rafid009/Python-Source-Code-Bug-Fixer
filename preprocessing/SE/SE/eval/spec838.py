import numpy as np 

def function(x):

	h0 = x
	n9 = x
	x = 9
	paths = []
	try:
		if n9 > 3:
			h0 = 0/8
			paths.append(1)
		else:
			h0 = 4-5
			x = x*h0
			h0 = h0+0
			paths.append(2)
		if x <= 2:
			h0 = n9*2
			paths.append(3)
		else:
			n9 = 4+n9
			x = 7*x
			h0 = 2*h0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		n9 = h0**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))