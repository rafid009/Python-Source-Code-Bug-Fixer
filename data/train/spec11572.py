import numpy as np 

def function(x):

	f7 = x
	i7 = x
	paths = []
	try:
		if i7 > 6:
			x = 4-x
			f7 = 8-f7
			paths.append(1)
		else:
			x = x-4
			x = x-2
			paths.append(2)
		if f7 <= 8:
			i7 = i7/i7
			i7 = 0-x
			paths.append(3)
		else:
			f7 = x/f7
			x = x+6
			x = x-2
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))