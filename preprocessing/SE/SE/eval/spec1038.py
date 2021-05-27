import numpy as np 

def function(x):

	n8 = x
	j0 = 8
	paths = []
	try:
		if n8 <= 4:
			j0 = n8+0
			paths.append(1)
		else:
			j0 = 2-j0
			paths.append(2)
		if x <= 5:
			x = 7/x
			paths.append(3)
		else:
			n8 = 4+n8
			n8 = 2*7
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		n8 = j0**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))