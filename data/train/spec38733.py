import numpy as np 

def function(x):

	h7 = x
	a1 = x
	paths = []
	try:
		if a1 > 3:
			h7 = x*4
			h7 = h7*0
			paths.append(1)
		else:
			h7 = x-4
			paths.append(2)
		if a1 > 7:
			a1 = a1+6
			a1 = 1+a1
			a1 = 6+a1
			paths.append(3)
		else:
			h7 = 1*h7
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