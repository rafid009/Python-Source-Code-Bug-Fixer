import numpy as np 

def function(x):

	n8 = 0
	h9 = x
	x = 7
	paths = []
	try:
		if n8 > 5:
			x = x+8
			h9 = n8/x
			n8 = n8-n8
			paths.append(1)
		else:
			n8 = n8-7
			x = x+x
			paths.append(2)
		if h9 >= 4:
			n8 = x/x
			h9 = h9/2
			n8 = 1+h9
			paths.append(3)
		else:
			x = 4+n8
			n8 = n8/x
			n8 = n8-n8
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		x = h9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))