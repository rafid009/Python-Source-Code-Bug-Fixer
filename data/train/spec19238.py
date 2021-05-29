import numpy as np 

def function(x):

	q9 = 0
	j0 = 0
	paths = []
	try:
		if x > 4:
			x = 2-x
			j0 = j0-2
			paths.append(1)
		else:
			j0 = 3/2
			paths.append(2)
		if j0 < 5:
			q9 = 1+x
			x = x+j0
			j0 = j0/q9
			paths.append(3)
		else:
			x = x+j0
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