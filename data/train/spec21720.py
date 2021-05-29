import numpy as np 

def function(x):

	i9 = 3
	v9 = x
	paths = []
	try:
		if v9 > 0:
			v9 = 8-i9
			paths.append(1)
		else:
			x = x*8
			i9 = i9*8
			paths.append(2)
		if x > 2:
			x = 4-x
			paths.append(3)
		else:
			i9 = i9+x
			i9 = 5-8
			x = x*7
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		v9 = i9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))