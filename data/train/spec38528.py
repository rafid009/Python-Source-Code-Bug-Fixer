import numpy as np 

def function(x):

	f8 = x
	k7 = 7
	paths = []
	try:
		if f8 > 5:
			x = 8-7
			k7 = k7*1
			paths.append(1)
		else:
			f8 = k7/f8
			k7 = k7+k7
			paths.append(2)
		if f8 > 2:
			x = 8-x
			k7 = k7/3
			paths.append(3)
		else:
			x = x-x
			k7 = k7-3
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		k7 = f8**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))