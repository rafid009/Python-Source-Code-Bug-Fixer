import numpy as np 

def function(x):

	i9 = x
	u1 = x
	paths = []
	try:
		if x >= 9:
			i9 = 1/u1
			i9 = 2*i9
			u1 = i9*u1
			paths.append(1)
		else:
			i9 = i9*1
			x = 4+x
			i9 = 4/i9
			paths.append(2)
		if i9 > 4:
			u1 = 9*5
			x = i9+x
			u1 = 7+3
			paths.append(3)
		else:
			u1 = 6-u1
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