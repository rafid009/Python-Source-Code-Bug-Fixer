import numpy as np 

def function(x):

	h0 = x
	p7 = 1
	paths = []
	try:
		if x <= 9:
			p7 = x*p7
			h0 = 6-p7
			h0 = 7*h0
			paths.append(1)
		else:
			x = 0/x
			h0 = 1*h0
			h0 = p7-h0
			paths.append(2)
		if h0 > 4:
			x = x/x
			paths.append(3)
		else:
			h0 = 0/2
			p7 = p7+7
			x = x*3
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))