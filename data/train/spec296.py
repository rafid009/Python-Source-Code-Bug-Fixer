import numpy as np 

def function(x):

	a9 = x
	n3 = x
	paths = []
	try:
		if x >= 1:
			x = 4-9
			n3 = n3-x
			paths.append(1)
		else:
			x = 4+x
			n3 = n3+a9
			paths.append(2)
		if x <= 4:
			n3 = 1-n3
			x = a9/a9
			x = 2+x
			paths.append(3)
		else:
			n3 = a9/a9
			x = x+8
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		a9 = n3**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))