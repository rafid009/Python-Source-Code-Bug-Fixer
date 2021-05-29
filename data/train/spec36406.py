import numpy as np 

def function(x):

	j1 = x
	i9 = 9
	paths = []
	try:
		if j1 > 0:
			j1 = j1*1
			paths.append(1)
		else:
			x = 5-8
			paths.append(2)
		if x <= 9:
			i9 = i9/j1
			paths.append(3)
		else:
			x = 7+4
			i9 = 9-i9
			i9 = 1-i9
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