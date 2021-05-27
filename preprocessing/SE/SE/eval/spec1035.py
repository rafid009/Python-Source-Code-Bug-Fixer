import numpy as np 

def function(x):

	j6 = 1
	a1 = 1
	paths = []
	try:
		if a1 >= 7:
			a1 = 9*a1
			j6 = 7/j6
			paths.append(1)
		else:
			j6 = 9/j6
			paths.append(2)
		if x <= 6:
			x = 4+x
			j6 = 6+2
			x = 1/x
			paths.append(3)
		else:
			x = x*0
			a1 = a1/3
			x = x-x
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