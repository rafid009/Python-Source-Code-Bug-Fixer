import numpy as np 

def function(x):

	j7 = 8
	i9 = x
	paths = []
	try:
		if j7 <= 1:
			x = i9+5
			j7 = i9-i9
			j7 = i9/i9
			paths.append(1)
		else:
			x = x+x
			i9 = i9+6
			paths.append(2)
		if i9 < 8:
			j7 = 3-6
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		i9 = j7**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))