import numpy as np 

def function(x):

	a5 = x
	q6 = x
	x = 5
	paths = []
	try:
		if a5 < 5:
			x = x+1
			q6 = q6+x
			paths.append(1)
		else:
			a5 = 9+x
			paths.append(2)
		if x >= 1:
			x = a5-6
			q6 = 6-q6
			q6 = 3/a5
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))