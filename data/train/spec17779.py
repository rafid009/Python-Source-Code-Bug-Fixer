import numpy as np 

def function(x):

	i6 = x
	h4 = 8
	paths = []
	try:
		if i6 > 6:
			h4 = h4-h4
			h4 = 8-h4
			x = x+1
			paths.append(1)
		else:
			h4 = 4*0
			h4 = h4/8
			x = 4*6
			paths.append(2)
		if h4 < 8:
			x = h4-i6
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		h4 = i6**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))