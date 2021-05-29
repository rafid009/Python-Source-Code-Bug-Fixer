import numpy as np 

def function(x):

	j2 = x
	h9 = 8
	paths = []
	try:
		if j2 > 6:
			x = x/j2
			j2 = j2-j2
			j2 = h9+j2
			paths.append(1)
		else:
			x = x+6
			j2 = j2-2
			paths.append(2)
		if h9 >= 1:
			x = 6/x
			h9 = 2-h9
			paths.append(3)
		else:
			j2 = 5/9
			j2 = 4+8
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))