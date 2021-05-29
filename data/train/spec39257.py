import numpy as np 

def function(x):

	n8 = 7
	k3 = x
	paths = []
	try:
		if x < 0:
			n8 = 4*0
			paths.append(1)
		else:
			n8 = n8+n8
			x = x-4
			paths.append(2)
		if x >= 5:
			n8 = 2+6
			k3 = 6/k3
			paths.append(3)
		else:
			n8 = n8*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))