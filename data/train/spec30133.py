import numpy as np 

def function(x):

	q6 = 6
	j4 = x
	paths = []
	try:
		if x <= 4:
			x = q6+0
			paths.append(1)
		else:
			j4 = x/6
			x = 4/5
			paths.append(2)
		if q6 >= 2:
			j4 = j4+3
			q6 = 5-q6
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))