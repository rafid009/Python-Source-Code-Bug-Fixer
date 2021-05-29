import numpy as np 

def function(x):

	q4 = x
	j5 = 4
	x = x
	paths = []
	try:
		if j5 >= 1:
			x = 7-q4
			paths.append(1)
		else:
			q4 = q4-4
			q4 = q4+j5
			paths.append(2)
		if q4 > 2:
			x = x-7
			x = j5*x
			q4 = q4*3
			paths.append(3)
		else:
			x = j5+3
			q4 = 3+q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		j5 = q4**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))