import numpy as np 

def function(x):

	q6 = x
	i7 = x
	paths = []
	try:
		if i7 > 2:
			i7 = 4/x
			x = x-1
			i7 = 2/i7
			paths.append(1)
		else:
			x = 3/9
			q6 = 2/q6
			x = 5+i7
			paths.append(2)
		if x > 2:
			q6 = 4/q6
			x = x-4
			paths.append(3)
		else:
			q6 = x/q6
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		q6 = i7**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))