import numpy as np 

def function(x):

	i7 = 1
	n5 = x
	x = 7
	paths = []
	try:
		if i7 < 4:
			i7 = 7/i7
			paths.append(1)
		else:
			x = 8-x
			x = x/x
			paths.append(2)
		if x >= 7:
			x = 5-i7
			paths.append(3)
		else:
			i7 = i7*8
			i7 = 7+n5
			i7 = i7+9
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