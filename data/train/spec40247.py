import numpy as np 

def function(x):

	i6 = 9
	i4 = x
	paths = []
	try:
		if i4 < 9:
			i6 = 7-8
			paths.append(1)
		else:
			i6 = i6/1
			i6 = x+i4
			paths.append(2)
		if i6 >= 2:
			i4 = 0-i4
			paths.append(3)
		else:
			i6 = i6-0
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))