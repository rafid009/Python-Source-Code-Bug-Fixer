import numpy as np 

def function(x):

	h7 = 7
	a1 = x
	paths = []
	try:
		if h7 <= 5:
			h7 = x*4
			h7 = h7/h7
			x = x+8
			paths.append(1)
		else:
			a1 = x-a1
			x = h7-h7
			paths.append(2)
		if a1 < 2:
			a1 = 2/6
			h7 = 6-h7
			x = 9*x
			paths.append(3)
		else:
			h7 = 7+x
			a1 = 9*a1
			h7 = a1+9
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