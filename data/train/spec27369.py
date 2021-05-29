import numpy as np 

def function(x):

	h7 = 1
	x9 = x
	paths = []
	try:
		if x9 <= 3:
			h7 = 2*h7
			paths.append(1)
		else:
			h7 = 4*2
			x9 = h7*h7
			h7 = 9*h7
			paths.append(2)
		if h7 >= 6:
			h7 = x9+x9
			x = 1+2
			paths.append(3)
		else:
			x = x+1
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))