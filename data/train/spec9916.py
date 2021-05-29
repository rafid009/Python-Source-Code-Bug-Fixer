import numpy as np 

def function(x):

	a4 = x
	q9 = x
	paths = []
	try:
		if q9 >= 5:
			a4 = 7-a4
			a4 = a4+9
			q9 = 5/q9
			paths.append(1)
		else:
			x = x-a4
			paths.append(2)
		if q9 <= 8:
			a4 = a4+a4
			x = x/a4
			paths.append(3)
		else:
			q9 = q9-4
			x = 1/a4
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		a4 = q9**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))