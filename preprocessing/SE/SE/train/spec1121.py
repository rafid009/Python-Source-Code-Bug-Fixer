import numpy as np 

def function(x):

	q9 = 5
	a1 = 7
	paths = []
	try:
		if x <= 0:
			x = x/a1
			a1 = a1+0
			x = x/6
			paths.append(1)
		else:
			a1 = a1+x
			a1 = 2-a1
			q9 = q9/a1
			paths.append(2)
		if x >= 7:
			x = 2/5
			a1 = 3/a1
			paths.append(3)
		else:
			x = 9+4
			x = 5+a1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))