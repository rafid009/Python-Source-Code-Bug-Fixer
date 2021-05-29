import numpy as np 

def function(x):

	k3 = 9
	y4 = 7
	paths = []
	try:
		if x < 3:
			x = x*y4
			paths.append(1)
		else:
			k3 = 8-7
			paths.append(2)
		if k3 > 2:
			y4 = y4-2
			k3 = k3*1
			y4 = 6+y4
			paths.append(3)
		else:
			k3 = k3+1
			y4 = 2+y4
			k3 = k3+k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))