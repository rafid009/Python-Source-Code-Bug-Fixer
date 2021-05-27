import numpy as np 

def function(x):

	j0 = 8
	a1 = 7
	paths = []
	try:
		if a1 > 7:
			x = x*j0
			paths.append(1)
		else:
			a1 = 3-a1
			j0 = a1*9
			x = x-9
			paths.append(2)
		if x > 2:
			x = x*7
			j0 = 1+a1
			x = 8*6
			paths.append(3)
		else:
			j0 = j0+0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))