import numpy as np 

def function(x):

	t6 = x
	h5 = 4
	paths = []
	try:
		if x >= 9:
			h5 = h5*1
			h5 = 1+0
			paths.append(1)
		else:
			h5 = t6+1
			t6 = 3/t6
			paths.append(2)
		if h5 <= 3:
			x = 4/x
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))