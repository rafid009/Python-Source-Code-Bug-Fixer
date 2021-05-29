import numpy as np 

def function(x):

	j2 = x
	h7 = x
	x = x
	paths = []
	try:
		if h7 >= 6:
			j2 = j2*2
			x = 1*7
			paths.append(1)
		else:
			h7 = h7+j2
			x = 7-j2
			paths.append(2)
		if h7 >= 3:
			x = h7+x
			paths.append(3)
		else:
			j2 = j2/7
			h7 = h7-1
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))