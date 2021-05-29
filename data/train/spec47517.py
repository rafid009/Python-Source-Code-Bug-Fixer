import numpy as np 

def function(x):

	h8 = x
	a9 = 4
	paths = []
	try:
		if a9 >= 7:
			a9 = a9/1
			x = x/2
			h8 = h8+5
			paths.append(1)
		else:
			x = 3+h8
			paths.append(2)
		if a9 <= 0:
			x = a9-x
			paths.append(3)
		else:
			x = 4+2
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		a9 = h8**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))