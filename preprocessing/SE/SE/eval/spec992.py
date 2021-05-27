import numpy as np 

def function(x):

	a8 = x
	j0 = 5
	paths = []
	try:
		if j0 >= 7:
			x = x*2
			a8 = a8*x
			j0 = 8-j0
			paths.append(1)
		else:
			x = x*x
			x = 1-j0
			paths.append(2)
		if x > 7:
			j0 = j0-j0
			a8 = 0-9
			a8 = 5*a8
			paths.append(3)
		else:
			x = 5/x
			j0 = j0+7
			a8 = x-a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		j0 = a8**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))