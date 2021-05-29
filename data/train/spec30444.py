import numpy as np 

def function(x):

	a7 = x
	j2 = 6
	paths = []
	try:
		if a7 > 2:
			a7 = 9-a7
			paths.append(1)
		else:
			a7 = j2-8
			paths.append(2)
		if j2 > 2:
			a7 = a7+0
			j2 = 3*4
			paths.append(3)
		else:
			a7 = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))