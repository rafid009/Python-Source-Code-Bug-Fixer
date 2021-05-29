import numpy as np 

def function(x):

	y6 = x
	n6 = x
	paths = []
	try:
		if y6 >= 5:
			x = 7/5
			y6 = 7+0
			paths.append(1)
		else:
			n6 = n6+x
			y6 = y6*9
			x = x+8
			paths.append(2)
		if x >= 1:
			n6 = 0/8
			x = x-6
			n6 = 0*1
			paths.append(3)
		else:
			x = 2+x
			y6 = 4-y6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))