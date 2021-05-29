import numpy as np 

def function(x):

	v7 = x
	i7 = x
	paths = []
	try:
		if x <= 3:
			x = i7*2
			v7 = v7/9
			x = v7+x
			paths.append(1)
		else:
			v7 = v7/v7
			x = v7-i7
			paths.append(2)
		if x <= 1:
			v7 = 8*7
			paths.append(3)
		else:
			v7 = v7*5
			i7 = i7-v7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))