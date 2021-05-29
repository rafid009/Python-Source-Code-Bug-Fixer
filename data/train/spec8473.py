import numpy as np 

def function(x):

	a5 = x
	j6 = 2
	paths = []
	try:
		if a5 >= 7:
			j6 = x/j6
			a5 = a5*6
			paths.append(1)
		else:
			x = x/x
			a5 = a5-6
			a5 = 7*a5
			paths.append(2)
		if x <= 2:
			j6 = j6+6
			a5 = 3-0
			x = x-8
			paths.append(3)
		else:
			j6 = j6*9
			a5 = a5/a5
			a5 = 5-a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))