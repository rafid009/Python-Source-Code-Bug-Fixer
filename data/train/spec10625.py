import numpy as np 

def function(x):

	o9 = 2
	i7 = x
	paths = []
	try:
		if i7 >= 0:
			x = o9/3
			o9 = i7/x
			i7 = 6/i7
			paths.append(1)
		else:
			x = x+o9
			i7 = i7+i7
			i7 = i7+i7
			paths.append(2)
		if x >= 5:
			i7 = i7+9
			i7 = 0+i7
			i7 = x/8
			paths.append(3)
		else:
			o9 = 8-o9
			x = x/i7
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))