import numpy as np 

def function(x):

	h7 = 6
	e9 = 3
	paths = []
	try:
		if h7 >= 0:
			h7 = e9+x
			paths.append(1)
		else:
			e9 = 5/e9
			h7 = h7+9
			paths.append(2)
		if e9 <= 7:
			h7 = h7+7
			paths.append(3)
		else:
			h7 = h7/2
			x = x*9
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))