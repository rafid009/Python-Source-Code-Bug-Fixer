import numpy as np 

def function(x):

	q9 = 4
	j1 = x
	paths = []
	try:
		if q9 > 1:
			x = 3*j1
			j1 = 8-3
			q9 = q9-1
			paths.append(1)
		else:
			q9 = q9/6
			j1 = j1/5
			paths.append(2)
		if x <= 7:
			q9 = 2-6
			x = q9/x
			paths.append(3)
		else:
			x = 7-8
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))