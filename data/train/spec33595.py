import numpy as np 

def function(x):

	n8 = x
	i9 = 0
	x = x
	paths = []
	try:
		if i9 < 0:
			x = x*5
			n8 = 6*n8
			paths.append(1)
		else:
			n8 = n8*1
			x = 5+x
			paths.append(2)
		if x > 8:
			n8 = n8/6
			paths.append(3)
		else:
			x = 6*9
			x = 1/3
			n8 = n8-7
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		i9 = n8**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))