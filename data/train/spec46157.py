import numpy as np 

def function(x):

	q9 = x
	j6 = x
	x = 2
	paths = []
	try:
		if q9 > 2:
			q9 = 7-9
			q9 = q9/j6
			x = x-9
			paths.append(1)
		else:
			x = j6+9
			x = 5-q9
			paths.append(2)
		if q9 >= 0:
			q9 = 0+x
			j6 = 5-j6
			paths.append(3)
		else:
			q9 = q9+x
			j6 = j6-0
			x = q9*3
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		q9 = j6**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))