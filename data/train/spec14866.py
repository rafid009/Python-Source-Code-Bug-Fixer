import numpy as np 

def function(x):

	k2 = 6
	c1 = x
	paths = []
	try:
		if c1 <= 3:
			k2 = 3+c1
			paths.append(1)
		else:
			x = x-x
			k2 = k2*4
			paths.append(2)
		if k2 > 2:
			x = x/7
			k2 = k2/2
			paths.append(3)
		else:
			x = 7*0
			x = 6/4
			x = 8-4
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))