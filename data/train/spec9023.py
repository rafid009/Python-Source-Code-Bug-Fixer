import numpy as np 

def function(x):

	k9 = x
	i8 = x
	x = 4
	paths = []
	try:
		if x <= 6:
			x = x/8
			x = x+x
			paths.append(1)
		else:
			i8 = 9*i8
			paths.append(2)
		if i8 < 2:
			i8 = i8/3
			i8 = 3-7
			x = x+k9
			paths.append(3)
		else:
			i8 = 3/i8
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))