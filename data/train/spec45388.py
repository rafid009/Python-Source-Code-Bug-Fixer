import numpy as np 

def function(x):

	i9 = 4
	f8 = 6
	paths = []
	try:
		if f8 > 3:
			i9 = 2-i9
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x <= 3:
			x = x/f8
			f8 = i9-x
			f8 = f8-x
			paths.append(3)
		else:
			i9 = f8-5
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))