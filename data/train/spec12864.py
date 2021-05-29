import numpy as np 

def function(x):

	a4 = x
	i8 = x
	x = x
	paths = []
	try:
		if a4 > 7:
			x = x-1
			i8 = a4*x
			a4 = a4-1
			paths.append(1)
		else:
			i8 = i8+i8
			a4 = 0*a4
			i8 = 1+a4
			paths.append(2)
		if i8 <= 3:
			a4 = 5+8
			i8 = a4+i8
			paths.append(3)
		else:
			x = 5-2
			i8 = x-i8
			a4 = a4/x
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		a4 = i8**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))