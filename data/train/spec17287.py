import numpy as np 

def function(x):

	i9 = x
	j8 = x
	paths = []
	try:
		if j8 > 0:
			x = x+i9
			x = 9/i9
			paths.append(1)
		else:
			j8 = j8-j8
			x = x+i9
			paths.append(2)
		if i9 < 3:
			j8 = x+j8
			paths.append(3)
		else:
			i9 = i9/x
			i9 = i9/i9
			j8 = x+j8
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))