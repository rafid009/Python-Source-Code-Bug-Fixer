import numpy as np 

def function(x):

	k5 = 6
	u8 = x
	paths = []
	try:
		if x >= 5:
			x = x+1
			k5 = 1*k5
			k5 = u8+k5
			paths.append(1)
		else:
			k5 = 2/k5
			k5 = 1/k5
			paths.append(2)
		if k5 >= 0:
			x = 4+0
			paths.append(3)
		else:
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))