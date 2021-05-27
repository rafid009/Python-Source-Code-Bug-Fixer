import numpy as np 

def function(x):

	d2 = 2
	h8 = x
	paths = []
	try:
		if h8 >= 3:
			x = 4+x
			h8 = h8+d2
			paths.append(1)
		else:
			x = x+4
			x = d2*1
			paths.append(2)
		if d2 >= 7:
			d2 = d2-0
			h8 = 2+5
			d2 = d2-4
			paths.append(3)
		else:
			d2 = 7+d2
			x = 3/8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))