import numpy as np 

def function(x):

	n3 = 0
	k2 = 3
	paths = []
	try:
		if k2 < 3:
			x = x-8
			n3 = n3*k2
			k2 = 8+k2
			paths.append(1)
		else:
			k2 = 5/k2
			paths.append(2)
		if n3 > 7:
			x = 9*x
			k2 = 4+x
			x = 1-x
			paths.append(3)
		else:
			n3 = n3-x
			x = x/n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))