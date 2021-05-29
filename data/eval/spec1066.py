import numpy as np 

def function(x):

	h3 = x
	b0 = x
	paths = []
	try:
		if b0 < 0:
			x = x-b0
			paths.append(1)
		else:
			x = x/3
			h3 = h3+8
			paths.append(2)
		if x >= 7:
			b0 = 7+h3
			h3 = 2+5
			h3 = b0/9
			paths.append(3)
		else:
			x = b0+x
			h3 = 0+h3
			b0 = 4-b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))