import numpy as np 

def function(x):

	i8 = x
	n3 = x
	paths = []
	try:
		if x > 1:
			i8 = i8+i8
			i8 = 9*7
			n3 = 5/n3
			paths.append(1)
		else:
			n3 = i8-8
			x = 9*n3
			n3 = 7*n3
			paths.append(2)
		if x >= 7:
			n3 = 1*n3
			x = 9*1
			paths.append(3)
		else:
			n3 = i8-0
			i8 = i8*x
			n3 = 1*6
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))