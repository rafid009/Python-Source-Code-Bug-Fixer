import numpy as np 

def function(x):

	n9 = x
	i6 = x
	paths = []
	try:
		if i6 < 2:
			x = x-x
			i6 = i6-0
			paths.append(1)
		else:
			n9 = n9+n9
			i6 = i6+n9
			paths.append(2)
		if x < 2:
			i6 = 6/6
			paths.append(3)
		else:
			n9 = 2+n9
			n9 = n9-7
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		i6 = n9**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))