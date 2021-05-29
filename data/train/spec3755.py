import numpy as np 

def function(x):

	k7 = x
	y3 = x
	paths = []
	try:
		if y3 >= 9:
			y3 = 7+y3
			x = x+4
			k7 = 9+7
			paths.append(1)
		else:
			x = x/y3
			paths.append(2)
		if x <= 4:
			x = 2/6
			y3 = 9+y3
			paths.append(3)
		else:
			x = 4+1
			y3 = 7-5
			k7 = k7+y3
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