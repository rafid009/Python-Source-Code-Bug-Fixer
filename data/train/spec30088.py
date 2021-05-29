import numpy as np 

def function(x):

	j4 = x
	a9 = x
	paths = []
	try:
		if j4 < 3:
			a9 = a9*a9
			paths.append(1)
		else:
			j4 = a9/3
			x = x/4
			paths.append(2)
		if j4 <= 5:
			x = 7+j4
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))