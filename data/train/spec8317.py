import numpy as np 

def function(x):

	k3 = 0
	u4 = x
	paths = []
	try:
		if x < 0:
			x = x+x
			u4 = k3+u4
			u4 = 7/1
			paths.append(1)
		else:
			u4 = 9+u4
			paths.append(2)
		if x <= 3:
			u4 = 1*x
			x = x/2
			paths.append(3)
		else:
			k3 = 4+k3
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))