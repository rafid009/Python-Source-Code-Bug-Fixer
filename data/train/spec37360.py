import numpy as np 

def function(x):

	i9 = x
	b1 = x
	x = 4
	paths = []
	try:
		if i9 < 5:
			i9 = i9*8
			b1 = i9+4
			paths.append(1)
		else:
			i9 = i9*1
			paths.append(2)
		if x < 3:
			x = 8*b1
			paths.append(3)
		else:
			b1 = 1*b1
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