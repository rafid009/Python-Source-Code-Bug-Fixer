import numpy as np 

def function(x):

	y5 = 1
	k5 = x
	paths = []
	try:
		if x > 9:
			y5 = y5-k5
			y5 = 7/2
			y5 = 9-y5
			paths.append(1)
		else:
			x = y5+x
			x = k5/y5
			x = x/k5
			paths.append(2)
		if y5 < 3:
			y5 = x*y5
			x = 7*x
			paths.append(3)
		else:
			k5 = k5/3
			k5 = x*8
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))