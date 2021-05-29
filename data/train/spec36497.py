import numpy as np 

def function(x):

	i4 = 0
	i7 = x
	paths = []
	try:
		if i7 >= 5:
			i7 = i4-i7
			i4 = 0+i7
			paths.append(1)
		else:
			i7 = 1/3
			i7 = 9*i7
			i4 = 0*i7
			paths.append(2)
		if i4 > 3:
			x = 8*4
			x = i7*i7
			x = 3/x
			paths.append(3)
		else:
			i7 = i7+i4
			i4 = i4-8
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))