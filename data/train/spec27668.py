import numpy as np 

def function(x):

	v4 = 2
	h2 = 4
	paths = []
	try:
		if v4 <= 4:
			h2 = 9-x
			v4 = 1-v4
			x = 8/h2
			paths.append(1)
		else:
			x = 8/x
			v4 = 1*1
			paths.append(2)
		if v4 < 2:
			h2 = h2+5
			h2 = h2/3
			h2 = x*1
			paths.append(3)
		else:
			h2 = h2-2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))