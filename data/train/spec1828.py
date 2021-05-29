import numpy as np 

def function(x):

	l6 = 2
	i8 = 5
	paths = []
	try:
		if l6 < 7:
			i8 = 3+i8
			paths.append(1)
		else:
			x = 8/1
			i8 = i8+i8
			paths.append(2)
		if l6 < 5:
			x = 2+x
			x = x+i8
			x = l6-6
			paths.append(3)
		else:
			x = 3*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))