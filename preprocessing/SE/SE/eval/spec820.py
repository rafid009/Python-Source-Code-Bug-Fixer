import numpy as np 

def function(x):

	g3 = x
	n8 = 5
	paths = []
	try:
		if g3 <= 3:
			n8 = 0+n8
			paths.append(1)
		else:
			n8 = 2/n8
			n8 = x-n8
			paths.append(2)
		if n8 <= 9:
			n8 = 6+0
			x = n8+7
			x = 0-1
			paths.append(3)
		else:
			n8 = x+n8
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		n8 = g3**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))