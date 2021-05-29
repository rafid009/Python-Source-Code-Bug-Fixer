import numpy as np 

def function(x):

	j1 = 2
	h0 = 9
	paths = []
	try:
		if x >= 6:
			x = h0/4
			j1 = 7/x
			paths.append(1)
		else:
			j1 = j1-0
			paths.append(2)
		if j1 > 4:
			x = x+6
			paths.append(3)
		else:
			h0 = 7+x
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		j1 = h0**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))