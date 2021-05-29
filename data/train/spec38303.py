import numpy as np 

def function(x):

	x2 = 0
	n3 = 9
	paths = []
	try:
		if x2 < 8:
			n3 = x-x2
			x = 4-x
			x = 3*9
			paths.append(1)
		else:
			x2 = x/x2
			x2 = n3/x2
			x2 = x2/5
			paths.append(2)
		if x < 4:
			n3 = n3/5
			x2 = x2*x
			paths.append(3)
		else:
			x2 = x2/n3
			x2 = x2/3
			n3 = 6-n3
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