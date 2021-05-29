import numpy as np 

def function(x):

	i8 = 4
	j7 = 3
	paths = []
	try:
		if i8 <= 9:
			j7 = 2-x
			paths.append(1)
		else:
			i8 = 9*6
			i8 = i8-7
			x = 5/3
			paths.append(2)
		if x <= 0:
			i8 = 5+5
			j7 = x/8
			paths.append(3)
		else:
			j7 = j7*j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))