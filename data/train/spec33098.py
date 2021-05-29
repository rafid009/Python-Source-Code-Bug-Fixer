import numpy as np 

def function(x):

	h8 = x
	b3 = 4
	paths = []
	try:
		if h8 < 5:
			h8 = h8*7
			x = 5*x
			x = 5*x
			paths.append(1)
		else:
			h8 = b3-0
			x = 5/9
			h8 = h8/h8
			paths.append(2)
		if b3 < 4:
			h8 = 1+9
			x = x-x
			paths.append(3)
		else:
			b3 = b3*3
			h8 = 3*h8
			b3 = x/5
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		b3 = h8**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))