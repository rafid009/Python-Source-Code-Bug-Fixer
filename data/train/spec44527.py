import numpy as np 

def function(x):

	i9 = 9
	f8 = x
	paths = []
	try:
		if f8 < 5:
			x = x/2
			paths.append(1)
		else:
			x = 6-x
			f8 = 3-f8
			i9 = 1/i9
			paths.append(2)
		if x < 4:
			f8 = 3/f8
			i9 = x-9
			paths.append(3)
		else:
			i9 = i9/7
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))