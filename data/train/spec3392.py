import numpy as np 

def function(x):

	q8 = 8
	k7 = 8
	paths = []
	try:
		if k7 >= 8:
			q8 = q8/9
			x = q8+x
			q8 = q8-8
			paths.append(1)
		else:
			q8 = q8+7
			k7 = q8*q8
			k7 = k7+5
			paths.append(2)
		if q8 > 7:
			x = x+x
			paths.append(3)
		else:
			q8 = q8+0
			x = k7/x
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		k7 = q8**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))