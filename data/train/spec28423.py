import numpy as np 

def function(x):

	j3 = 5
	h8 = 4
	paths = []
	try:
		if j3 < 4:
			x = 4-x
			j3 = 4+x
			j3 = j3+0
			paths.append(1)
		else:
			j3 = 2*9
			j3 = x-6
			paths.append(2)
		if h8 < 3:
			h8 = 3+3
			x = x*2
			j3 = h8-j3
			paths.append(3)
		else:
			h8 = x*h8
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