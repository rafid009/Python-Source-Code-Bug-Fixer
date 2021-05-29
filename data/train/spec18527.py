import numpy as np 

def function(x):

	i7 = x
	n8 = 8
	paths = []
	try:
		if x >= 8:
			x = x/2
			i7 = n8/8
			x = x-9
			paths.append(1)
		else:
			n8 = n8+0
			x = 8*x
			n8 = n8/9
			paths.append(2)
		if n8 > 9:
			x = n8/7
			i7 = i7-n8
			n8 = 9-n8
			paths.append(3)
		else:
			n8 = 3+n8
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))