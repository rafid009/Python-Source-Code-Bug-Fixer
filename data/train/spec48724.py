import numpy as np 

def function(x):

	i4 = 1
	a8 = 4
	paths = []
	try:
		if i4 > 9:
			i4 = i4-9
			x = x*2
			a8 = 7-a8
			paths.append(1)
		else:
			i4 = 5+x
			a8 = a8*a8
			x = x+a8
			paths.append(2)
		if a8 >= 1:
			i4 = 3-x
			x = a8*9
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		a8 = i4**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))