import numpy as np 

def function(x):

	o2 = 4
	i9 = x
	x = 6
	paths = []
	try:
		if i9 >= 6:
			o2 = 6*o2
			i9 = o2/8
			i9 = 0-4
			paths.append(1)
		else:
			x = i9/3
			i9 = 0+i9
			paths.append(2)
		if x < 3:
			i9 = i9+x
			o2 = 0-o2
			paths.append(3)
		else:
			o2 = o2/8
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		i9 = o2**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))