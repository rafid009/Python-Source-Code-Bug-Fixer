import numpy as np 

def function(x):

	h8 = 5
	e7 = 0
	paths = []
	try:
		if e7 <= 4:
			h8 = 6*h8
			paths.append(1)
		else:
			x = 8+x
			e7 = h8+e7
			paths.append(2)
		if e7 <= 4:
			h8 = x*h8
			paths.append(3)
		else:
			h8 = x+h8
			e7 = 0-e7
			x = x/1
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