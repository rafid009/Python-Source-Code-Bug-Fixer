import numpy as np 

def function(x):

	j6 = 5
	a5 = 2
	paths = []
	try:
		if j6 <= 0:
			a5 = a5+j6
			a5 = 0/a5
			paths.append(1)
		else:
			j6 = j6-7
			paths.append(2)
		if a5 <= 0:
			x = j6+x
			x = 1*x
			paths.append(3)
		else:
			a5 = a5-3
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