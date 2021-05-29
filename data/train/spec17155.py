import numpy as np 

def function(x):

	y4 = 1
	k5 = x
	paths = []
	try:
		if x > 8:
			x = x+4
			x = 7-6
			y4 = y4*8
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x <= 4:
			y4 = 4*y4
			k5 = k5/1
			paths.append(3)
		else:
			k5 = x+k5
			x = 5+y4
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))