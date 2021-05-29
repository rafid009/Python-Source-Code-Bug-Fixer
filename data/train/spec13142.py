import numpy as np 

def function(x):

	q4 = x
	j4 = 4
	x = x
	paths = []
	try:
		if q4 > 1:
			j4 = 9-j4
			x = 8+x
			x = 5/x
			paths.append(1)
		else:
			j4 = 5/j4
			x = x*0
			paths.append(2)
		if q4 < 2:
			j4 = x-x
			q4 = q4+9
			paths.append(3)
		else:
			q4 = 7/q4
			x = x+x
			x = 3-6
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))