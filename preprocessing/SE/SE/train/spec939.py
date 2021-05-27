import numpy as np 

def function(x):

	b4 = x
	h0 = x
	paths = []
	try:
		if b4 >= 2:
			x = 0/7
			x = x+2
			paths.append(1)
		else:
			x = b4+8
			h0 = h0+9
			paths.append(2)
		if b4 <= 8:
			x = h0*6
			x = x*2
			paths.append(3)
		else:
			b4 = x*1
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))