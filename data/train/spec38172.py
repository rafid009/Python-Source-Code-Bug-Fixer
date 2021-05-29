import numpy as np 

def function(x):

	h7 = 7
	v9 = x
	x = 8
	paths = []
	try:
		if x >= 9:
			v9 = 3+v9
			v9 = x+4
			v9 = v9/1
			paths.append(1)
		else:
			h7 = h7/6
			x = 9/x
			x = x-x
			paths.append(2)
		if x < 2:
			h7 = 7+h7
			v9 = 1+v9
			v9 = 2+v9
			paths.append(3)
		else:
			x = x*x
			v9 = 7-h7
			h7 = h7/v9
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		h7 = v9**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))