import numpy as np 

def function(x):

	u0 = x
	i9 = x
	x = x
	paths = []
	try:
		if i9 >= 3:
			i9 = x-9
			paths.append(1)
		else:
			i9 = u0+i9
			x = x-1
			paths.append(2)
		if u0 <= 7:
			i9 = 1/i9
			x = x/x
			x = i9+7
			paths.append(3)
		else:
			u0 = x/u0
			u0 = u0+2
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		u0 = i9**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))