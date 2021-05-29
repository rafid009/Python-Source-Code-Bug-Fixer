import numpy as np 

def function(x):

	n3 = x
	r9 = 4
	paths = []
	try:
		if r9 <= 6:
			x = n3+7
			r9 = n3/n3
			paths.append(1)
		else:
			n3 = 9+n3
			x = 8*5
			paths.append(2)
		if x < 0:
			x = x+x
			x = x+6
			x = 9/x
			paths.append(3)
		else:
			x = 0+x
			n3 = n3-3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		r9 = n3**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))