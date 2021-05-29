import numpy as np 

def function(x):

	h7 = x
	j3 = 3
	paths = []
	try:
		if j3 >= 6:
			h7 = h7*h7
			j3 = j3/6
			h7 = 0/x
			paths.append(1)
		else:
			j3 = x-x
			h7 = 6+h7
			j3 = x+4
			paths.append(2)
		if h7 <= 8:
			x = 8/h7
			paths.append(3)
		else:
			h7 = 8-j3
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))