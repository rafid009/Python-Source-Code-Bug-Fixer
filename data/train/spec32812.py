import numpy as np 

def function(x):

	a0 = 1
	i8 = x
	paths = []
	try:
		if a0 >= 2:
			a0 = i8+x
			x = 9*6
			a0 = i8*a0
			paths.append(1)
		else:
			a0 = a0/8
			x = x/5
			i8 = x-2
			paths.append(2)
		if a0 > 2:
			x = x*a0
			i8 = 1+a0
			paths.append(3)
		else:
			a0 = 4+x
			i8 = i8-7
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		a0 = i8**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))