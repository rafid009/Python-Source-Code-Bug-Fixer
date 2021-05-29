import numpy as np 

def function(x):

	h7 = 8
	v3 = x
	paths = []
	try:
		if x >= 4:
			h7 = 7-5
			paths.append(1)
		else:
			v3 = x*7
			x = v3/x
			v3 = 3*v3
			paths.append(2)
		if x <= 5:
			v3 = x+6
			h7 = h7*1
			h7 = h7-2
			paths.append(3)
		else:
			x = x+x
			h7 = 3/v3
			v3 = v3-v3
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		h7 = h7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))