import numpy as np 

def function(x):

	h8 = 0
	j5 = x
	paths = []
	try:
		if x > 3:
			j5 = j5+4
			j5 = j5*h8
			paths.append(1)
		else:
			h8 = h8+4
			paths.append(2)
		if x > 9:
			h8 = j5-h8
			x = x/3
			paths.append(3)
		else:
			j5 = j5+x
			j5 = j5*1
			h8 = x*6
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))