import numpy as np 

def function(x):

	k7 = x
	y8 = 3
	paths = []
	try:
		if y8 > 4:
			y8 = 8*3
			paths.append(1)
		else:
			x = 9*1
			x = 8+x
			paths.append(2)
		if k7 < 7:
			x = x*2
			y8 = 6/4
			k7 = k7*6
			paths.append(3)
		else:
			k7 = k7/x
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