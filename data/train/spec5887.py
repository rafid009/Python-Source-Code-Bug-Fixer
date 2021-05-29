import numpy as np 

def function(x):

	j2 = 9
	i8 = 0
	paths = []
	try:
		if i8 < 9:
			i8 = i8*3
			j2 = 0/5
			j2 = x*8
			paths.append(1)
		else:
			x = 8/x
			j2 = 6/j2
			j2 = 4-j2
			paths.append(2)
		if j2 < 2:
			j2 = j2-5
			i8 = 0-i8
			paths.append(3)
		else:
			i8 = i8-i8
			x = 9-j2
			x = x+4
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