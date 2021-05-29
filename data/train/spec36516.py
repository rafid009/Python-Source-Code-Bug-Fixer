import numpy as np 

def function(x):

	i9 = x
	x5 = 9
	paths = []
	try:
		if i9 <= 8:
			x = x*3
			x = x+x5
			x5 = 3+x5
			paths.append(1)
		else:
			x = i9-4
			paths.append(2)
		if x5 >= 9:
			x5 = x5*9
			x5 = 1/1
			i9 = 6-i9
			paths.append(3)
		else:
			i9 = x5/i9
			x = i9+x
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