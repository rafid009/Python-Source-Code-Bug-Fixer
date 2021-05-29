import numpy as np 

def function(x):

	k1 = 4
	y7 = 1
	paths = []
	try:
		if x > 3:
			x = 7-x
			k1 = k1/9
			k1 = 4+x
			paths.append(1)
		else:
			x = 1-y7
			k1 = k1*7
			y7 = y7+3
			paths.append(2)
		if x <= 6:
			x = x-y7
			paths.append(3)
		else:
			y7 = y7+k1
			y7 = 2+6
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		y7 = k1**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))