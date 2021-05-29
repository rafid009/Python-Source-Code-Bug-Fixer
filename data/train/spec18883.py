import numpy as np 

def function(x):

	n8 = x
	h8 = 0
	paths = []
	try:
		if h8 > 1:
			x = 0*7
			x = x*1
			paths.append(1)
		else:
			x = 9-x
			h8 = h8*0
			n8 = 7+5
			paths.append(2)
		if x >= 4:
			x = 8*x
			n8 = 0/2
			paths.append(3)
		else:
			h8 = x*x
			h8 = 3-h8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		n8 = h8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))