import numpy as np 

def function(x):

	k2 = 8
	y7 = x
	paths = []
	try:
		if x <= 4:
			x = x*0
			y7 = k2-1
			paths.append(1)
		else:
			y7 = 9*k2
			paths.append(2)
		if x > 7:
			k2 = 0-k2
			paths.append(3)
		else:
			y7 = y7-8
			x = x/7
			y7 = k2/y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		k2 = y7**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))