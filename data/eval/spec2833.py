import numpy as np 

def function(x):

	f6 = x
	i9 = 5
	paths = []
	try:
		if f6 < 3:
			i9 = 3*i9
			f6 = 1/f6
			x = 9+i9
			paths.append(1)
		else:
			i9 = x*7
			paths.append(2)
		if f6 > 5:
			x = i9-f6
			i9 = i9*x
			paths.append(3)
		else:
			f6 = 3*f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		i9 = f6**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))