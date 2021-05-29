import numpy as np 

def function(x):

	i6 = x
	n5 = x
	paths = []
	try:
		if n5 < 6:
			i6 = 5+n5
			n5 = 2-n5
			paths.append(1)
		else:
			i6 = 3+i6
			paths.append(2)
		if n5 <= 5:
			i6 = n5+1
			paths.append(3)
		else:
			i6 = 5+n5
			x = x*5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))