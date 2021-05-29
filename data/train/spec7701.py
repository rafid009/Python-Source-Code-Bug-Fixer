import numpy as np 

def function(x):

	j6 = x
	a9 = x
	x = 9
	paths = []
	try:
		if x < 9:
			a9 = 0*a9
			j6 = j6+j6
			j6 = j6/j6
			paths.append(1)
		else:
			j6 = j6+9
			a9 = 6/2
			x = x*3
			paths.append(2)
		if x < 8:
			x = x-6
			a9 = 8*a9
			a9 = a9*x
			paths.append(3)
		else:
			j6 = 4+j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		a9 = j6**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))