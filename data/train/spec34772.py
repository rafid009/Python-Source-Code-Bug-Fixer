import numpy as np 

def function(x):

	k7 = x
	u8 = 5
	paths = []
	try:
		if k7 > 0:
			x = x/x
			k7 = k7-6
			paths.append(1)
		else:
			x = x/2
			x = x/5
			u8 = x*2
			paths.append(2)
		if u8 > 8:
			k7 = k7*k7
			u8 = u8-u8
			paths.append(3)
		else:
			x = u8+7
			u8 = u8-x
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