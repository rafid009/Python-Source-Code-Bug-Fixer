import numpy as np 

def function(x):

	h8 = x
	u6 = x
	paths = []
	try:
		if x >= 3:
			u6 = u6-x
			h8 = 6+h8
			paths.append(1)
		else:
			u6 = 5-7
			x = 3/h8
			paths.append(2)
		if h8 > 2:
			u6 = u6-x
			x = x*4
			paths.append(3)
		else:
			x = x+x
			x = u6/x
			x = u6/2
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))