import numpy as np 

def function(x):

	l3 = 0
	h0 = x
	x = 5
	paths = []
	try:
		if x < 7:
			l3 = 3+x
			l3 = l3-6
			paths.append(1)
		else:
			l3 = 3-l3
			h0 = 4/1
			l3 = l3/9
			paths.append(2)
		if h0 < 7:
			h0 = 7-x
			paths.append(3)
		else:
			l3 = 0-1
			h0 = h0/x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		h0 = l3**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))