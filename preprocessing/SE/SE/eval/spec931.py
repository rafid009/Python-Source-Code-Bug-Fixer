import numpy as np 

def function(x):

	k7 = 1
	c3 = x
	paths = []
	try:
		if x < 3:
			c3 = k7*c3
			x = 9-2
			paths.append(1)
		else:
			k7 = 0+4
			paths.append(2)
		if k7 <= 7:
			x = 5+c3
			k7 = c3*1
			c3 = 7+9
			paths.append(3)
		else:
			k7 = 8/k7
			k7 = k7*5
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))