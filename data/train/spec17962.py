import numpy as np 

def function(x):

	b2 = x
	h5 = 9
	paths = []
	try:
		if x < 1:
			h5 = 7-h5
			b2 = b2+3
			b2 = b2+b2
			paths.append(1)
		else:
			b2 = b2-7
			paths.append(2)
		if x < 5:
			h5 = h5*5
			x = 3-4
			paths.append(3)
		else:
			b2 = b2/h5
			h5 = b2+9
			x = x-x
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		b2 = h5**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))