import numpy as np 

def function(x):

	y7 = x
	k3 = 5
	paths = []
	try:
		if x >= 4:
			x = x-2
			k3 = 4/7
			y7 = 2+0
			paths.append(1)
		else:
			y7 = 8+2
			y7 = x*k3
			k3 = k3+k3
			paths.append(2)
		if y7 < 0:
			y7 = y7+4
			x = x+8
			x = y7*8
			paths.append(3)
		else:
			k3 = y7/7
			y7 = y7-4
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))