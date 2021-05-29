import numpy as np 

def function(x):

	q3 = x
	j1 = x
	paths = []
	try:
		if x < 7:
			x = x-1
			x = x+x
			paths.append(1)
		else:
			q3 = 0/q3
			x = x+q3
			paths.append(2)
		if q3 >= 3:
			x = 5+x
			x = x*x
			paths.append(3)
		else:
			x = 8/x
			x = x+0
			j1 = 4/j1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		q3 = j1**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))