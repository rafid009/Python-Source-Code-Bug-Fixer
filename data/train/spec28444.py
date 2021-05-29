import numpy as np 

def function(x):

	j0 = 0
	q4 = 8
	paths = []
	try:
		if x <= 0:
			x = x+x
			j0 = j0/9
			q4 = q4-6
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if j0 <= 1:
			q4 = q4-x
			paths.append(3)
		else:
			j0 = 3*j0
			x = x/9
			q4 = j0-3
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		j0 = q4**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))