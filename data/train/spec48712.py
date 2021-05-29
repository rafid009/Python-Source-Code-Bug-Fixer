import numpy as np 

def function(x):

	u1 = 7
	i7 = 3
	paths = []
	try:
		if x < 3:
			u1 = 5+u1
			i7 = i7*4
			i7 = 9-i7
			paths.append(1)
		else:
			i7 = i7*3
			paths.append(2)
		if x <= 1:
			i7 = i7*9
			u1 = 2+u1
			paths.append(3)
		else:
			u1 = u1/u1
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