import numpy as np 

def function(x):

	k7 = 4
	u4 = x
	paths = []
	try:
		if u4 > 7:
			k7 = k7*6
			u4 = 1-4
			paths.append(1)
		else:
			u4 = 2-x
			x = k7-1
			paths.append(2)
		if u4 > 0:
			k7 = 0*0
			paths.append(3)
		else:
			u4 = u4-9
			x = x-2
			k7 = 6-k7
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