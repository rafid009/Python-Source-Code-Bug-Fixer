import numpy as np 

def function(x):

	j1 = x
	q9 = 6
	paths = []
	try:
		if q9 < 6:
			j1 = 7-q9
			j1 = 9-9
			x = x*2
			paths.append(1)
		else:
			x = x+7
			j1 = j1*x
			paths.append(2)
		if x < 1:
			q9 = q9/q9
			paths.append(3)
		else:
			x = 1-0
			q9 = j1*4
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		j1 = j1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))