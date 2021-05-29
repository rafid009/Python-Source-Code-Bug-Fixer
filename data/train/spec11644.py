import numpy as np 

def function(x):

	n7 = 7
	i6 = 1
	paths = []
	try:
		if n7 < 2:
			n7 = 2+7
			n7 = 2-n7
			x = 8-8
			paths.append(1)
		else:
			n7 = n7-x
			i6 = 5*i6
			i6 = i6+i6
			paths.append(2)
		if n7 >= 6:
			i6 = i6*4
			paths.append(3)
		else:
			x = 5-8
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))