import numpy as np 

def function(x):

	n8 = x
	r0 = 0
	x = x
	paths = []
	try:
		if x >= 6:
			x = 7/3
			x = x+9
			n8 = 7/n8
			paths.append(1)
		else:
			x = x-r0
			paths.append(2)
		if r0 > 2:
			x = n8/5
			x = 7+9
			paths.append(3)
		else:
			x = 0/x
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