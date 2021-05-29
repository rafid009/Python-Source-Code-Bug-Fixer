import numpy as np 

def function(x):

	j1 = x
	h8 = 1
	paths = []
	try:
		if h8 < 9:
			j1 = j1/1
			j1 = h8+9
			h8 = j1+h8
			paths.append(1)
		else:
			x = h8*2
			j1 = x-8
			paths.append(2)
		if x < 2:
			h8 = x-h8
			j1 = 1+7
			j1 = j1-h8
			paths.append(3)
		else:
			h8 = 0-h8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		j1 = h8**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))