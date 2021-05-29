import numpy as np 

def function(x):

	x9 = 8
	n3 = x
	paths = []
	try:
		if x9 <= 9:
			x = x-x
			x = 3-x
			paths.append(1)
		else:
			x = x+x9
			paths.append(2)
		if x < 7:
			x = n3/4
			x = n3+1
			x9 = n3/x
			paths.append(3)
		else:
			n3 = 3-n3
			x = x-3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x9 = n3**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))