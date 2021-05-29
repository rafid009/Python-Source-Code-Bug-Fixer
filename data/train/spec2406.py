import numpy as np 

def function(x):

	i5 = 4
	h0 = 1
	x = 3
	paths = []
	try:
		if x < 3:
			x = x*2
			i5 = 3*i5
			i5 = h0/i5
			paths.append(1)
		else:
			h0 = h0-9
			i5 = h0/i5
			h0 = i5/x
			paths.append(2)
		if i5 >= 0:
			h0 = h0*6
			paths.append(3)
		else:
			x = 3+7
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))