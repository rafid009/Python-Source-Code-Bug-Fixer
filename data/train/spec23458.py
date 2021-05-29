import numpy as np 

def function(x):

	q9 = x
	j1 = x
	paths = []
	try:
		if q9 > 0:
			q9 = q9+q9
			q9 = q9+0
			paths.append(1)
		else:
			x = x*9
			x = 1/q9
			j1 = j1-4
			paths.append(2)
		if j1 < 9:
			x = j1*j1
			paths.append(3)
		else:
			q9 = q9*7
			x = 6-4
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))