import numpy as np 

def function(x):

	i8 = x
	a2 = x
	x = 9
	paths = []
	try:
		if i8 >= 0:
			a2 = 8+x
			i8 = i8*3
			paths.append(1)
		else:
			a2 = x/a2
			x = 2/x
			i8 = i8-7
			paths.append(2)
		if i8 >= 1:
			i8 = 3+i8
			i8 = i8/2
			paths.append(3)
		else:
			a2 = a2+7
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		a2 = i8**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))