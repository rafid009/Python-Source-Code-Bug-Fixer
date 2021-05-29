import numpy as np 

def function(x):

	h8 = x
	b3 = x
	paths = []
	try:
		if x <= 0:
			x = 5-x
			x = 4*5
			paths.append(1)
		else:
			x = 5+x
			h8 = h8/1
			b3 = 8/b3
			paths.append(2)
		if x < 6:
			x = 8+x
			x = 8+x
			h8 = h8*2
			paths.append(3)
		else:
			x = 0+h8
			b3 = b3*2
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))