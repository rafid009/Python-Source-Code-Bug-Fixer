import numpy as np 

def function(x):

	j0 = x
	i9 = 7
	paths = []
	try:
		if x < 9:
			x = 7-3
			x = j0-x
			i9 = i9+9
			paths.append(1)
		else:
			i9 = x/i9
			paths.append(2)
		if i9 <= 9:
			x = x*0
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		i9 = j0**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))