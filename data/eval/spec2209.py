import numpy as np 

def function(x):

	n9 = x
	i6 = x
	x = x
	paths = []
	try:
		if n9 > 8:
			x = n9+x
			i6 = 3*i6
			n9 = 0*n9
			paths.append(1)
		else:
			i6 = 2-5
			paths.append(2)
		if i6 >= 1:
			n9 = 5+6
			n9 = n9-9
			i6 = i6-n9
			paths.append(3)
		else:
			i6 = i6/x
			x = i6/i6
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		n9 = i6**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))