import numpy as np 

def function(x):

	n8 = x
	e9 = 1
	paths = []
	try:
		if n8 < 4:
			n8 = 0+3
			n8 = n8*4
			paths.append(1)
		else:
			n8 = n8/n8
			x = x+1
			paths.append(2)
		if n8 > 9:
			n8 = 0-6
			x = x+4
			e9 = 1+e9
			paths.append(3)
		else:
			e9 = e9/n8
			x = x+9
			x = x+9
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