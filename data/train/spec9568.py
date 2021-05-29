import numpy as np 

def function(x):

	h7 = 7
	k6 = x
	paths = []
	try:
		if k6 < 2:
			x = x*0
			k6 = 1/k6
			h7 = h7-2
			paths.append(1)
		else:
			k6 = 8*8
			h7 = h7-9
			paths.append(2)
		if k6 >= 1:
			h7 = 0-x
			k6 = k6-1
			x = x*1
			paths.append(3)
		else:
			h7 = h7*h7
			h7 = 9-7
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))