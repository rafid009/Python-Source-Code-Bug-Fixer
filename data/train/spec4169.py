import numpy as np 

def function(x):

	q4 = 6
	j4 = x
	paths = []
	try:
		if x > 9:
			j4 = 2+j4
			paths.append(1)
		else:
			j4 = j4+j4
			paths.append(2)
		if q4 < 5:
			q4 = q4/8
			q4 = q4-q4
			j4 = 4*q4
			paths.append(3)
		else:
			x = 7/x
			x = x/q4
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))