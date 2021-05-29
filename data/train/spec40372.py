import numpy as np 

def function(x):

	j2 = 9
	i9 = 3
	paths = []
	try:
		if j2 > 4:
			i9 = 1+7
			i9 = x+j2
			j2 = i9-j2
			paths.append(1)
		else:
			j2 = 3-j2
			j2 = i9/j2
			j2 = j2*9
			paths.append(2)
		if x >= 6:
			j2 = i9*i9
			i9 = 6-j2
			j2 = 2+j2
			paths.append(3)
		else:
			x = x/6
			j2 = 6/5
			x = 0-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))