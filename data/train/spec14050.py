import numpy as np 

def function(x):

	a3 = x
	n8 = x
	paths = []
	try:
		if x >= 7:
			a3 = 6-a3
			n8 = n8-0
			paths.append(1)
		else:
			x = a3*9
			n8 = 0-n8
			n8 = n8*3
			paths.append(2)
		if x < 3:
			n8 = n8*6
			a3 = 2+a3
			paths.append(3)
		else:
			a3 = a3-3
			n8 = n8*5
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		n8 = a3**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))