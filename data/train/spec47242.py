import numpy as np 

def function(x):

	k0 = 3
	y4 = 9
	x = x
	paths = []
	try:
		if x <= 7:
			y4 = y4-5
			x = x*y4
			paths.append(1)
		else:
			y4 = 4-y4
			y4 = y4+y4
			paths.append(2)
		if y4 < 5:
			k0 = k0+x
			paths.append(3)
		else:
			x = 0/6
			x = k0*3
			k0 = 4/k0
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))