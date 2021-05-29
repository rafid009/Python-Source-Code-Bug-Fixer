import numpy as np 

def function(x):

	f7 = x
	i8 = 7
	paths = []
	try:
		if f7 <= 2:
			f7 = f7*3
			paths.append(1)
		else:
			x = x+4
			x = 6*f7
			paths.append(2)
		if i8 <= 1:
			x = x*i8
			f7 = f7/x
			paths.append(3)
		else:
			i8 = i8*9
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		i8 = f7**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))