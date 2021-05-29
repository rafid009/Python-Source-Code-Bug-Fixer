import numpy as np 

def function(x):

	y0 = x
	n2 = x
	paths = []
	try:
		if n2 < 8:
			n2 = 5/n2
			x = 9+x
			paths.append(1)
		else:
			n2 = n2/x
			paths.append(2)
		if n2 >= 4:
			n2 = n2/5
			paths.append(3)
		else:
			n2 = n2+x
			x = 0-x
			y0 = 1*2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))