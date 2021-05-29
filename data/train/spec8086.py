import numpy as np 

def function(x):

	j6 = x
	q0 = 9
	paths = []
	try:
		if q0 > 6:
			x = x+j6
			x = j6-4
			paths.append(1)
		else:
			j6 = j6/j6
			j6 = j6/1
			paths.append(2)
		if q0 <= 4:
			j6 = 4*6
			paths.append(3)
		else:
			q0 = q0/x
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))