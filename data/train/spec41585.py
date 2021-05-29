import numpy as np 

def function(x):

	o8 = 0
	n3 = x
	paths = []
	try:
		if x <= 7:
			n3 = n3-o8
			n3 = n3*1
			paths.append(1)
		else:
			o8 = 7*n3
			n3 = 7+n3
			o8 = 1*o8
			paths.append(2)
		if n3 > 5:
			n3 = 6/n3
			o8 = o8+n3
			x = 8-x
			paths.append(3)
		else:
			n3 = 6*n3
			o8 = 5+o8
			n3 = n3/4
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))