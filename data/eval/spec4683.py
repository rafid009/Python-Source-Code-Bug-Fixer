import numpy as np 

def function(x):

	k1 = x
	h4 = 5
	paths = []
	try:
		if x >= 4:
			h4 = x/h4
			h4 = h4+h4
			h4 = h4/8
			paths.append(1)
		else:
			h4 = 2*k1
			h4 = h4*8
			k1 = k1*5
			paths.append(2)
		if k1 >= 6:
			x = k1-5
			x = k1/x
			paths.append(3)
		else:
			h4 = 6/h4
			k1 = 2-x
			k1 = k1-2
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		k1 = h4**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))