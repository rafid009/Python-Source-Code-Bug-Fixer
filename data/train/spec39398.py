import numpy as np 

def function(x):

	v7 = x
	h3 = 8
	paths = []
	try:
		if v7 <= 3:
			x = 4+x
			h3 = h3+9
			x = x+x
			paths.append(1)
		else:
			v7 = v7/v7
			h3 = h3/2
			x = 4-x
			paths.append(2)
		if v7 >= 3:
			v7 = x+v7
			paths.append(3)
		else:
			x = h3+1
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		h3 = v7**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))