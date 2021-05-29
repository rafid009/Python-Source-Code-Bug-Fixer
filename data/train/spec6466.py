import numpy as np 

def function(x):

	n3 = 7
	n2 = 7
	paths = []
	try:
		if n2 <= 9:
			n2 = n2+4
			n3 = 5/n3
			x = 8+x
			paths.append(1)
		else:
			x = x/3
			n3 = n3-x
			n2 = n2+n3
			paths.append(2)
		if n2 >= 6:
			n3 = 1-n3
			paths.append(3)
		else:
			n3 = 7/n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))