import numpy as np 

def function(x):

	k9 = 3
	i7 = x
	paths = []
	try:
		if k9 > 4:
			k9 = 5*k9
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x >= 5:
			k9 = 8/x
			x = x-9
			paths.append(3)
		else:
			k9 = 4-7
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