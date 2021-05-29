import numpy as np 

def function(x):

	j5 = x
	n8 = 6
	x = 7
	paths = []
	try:
		if x >= 0:
			n8 = 0-n8
			paths.append(1)
		else:
			n8 = x*8
			x = j5-3
			n8 = n8+n8
			paths.append(2)
		if n8 <= 9:
			j5 = 3+j5
			n8 = x/j5
			n8 = 2*n8
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))