import numpy as np 

def function(x):

	j2 = x
	j0 = x
	x = 3
	paths = []
	try:
		if j0 >= 2:
			j2 = 8/5
			paths.append(1)
		else:
			j2 = j2-6
			x = 4-j2
			paths.append(2)
		if x < 3:
			x = x+j0
			j2 = 7*j2
			j2 = j2-1
			paths.append(3)
		else:
			j2 = 3+0
			x = j0-0
			x = 6*j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))