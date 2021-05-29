import numpy as np 

def function(x):

	h7 = 0
	h1 = x
	paths = []
	try:
		if x < 7:
			h1 = h7+5
			h7 = x/9
			paths.append(1)
		else:
			h1 = 0+9
			h7 = h1-h1
			paths.append(2)
		if h7 <= 2:
			h7 = 6*h7
			paths.append(3)
		else:
			h1 = h1-2
			h1 = 7*h1
			h1 = 9/6
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