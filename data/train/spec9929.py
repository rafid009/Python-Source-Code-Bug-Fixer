import numpy as np 

def function(x):

	e7 = x
	q9 = 7
	paths = []
	try:
		if x > 5:
			q9 = 2+x
			e7 = q9/q9
			paths.append(1)
		else:
			q9 = q9-8
			x = x/9
			x = 5+3
			paths.append(2)
		if e7 > 7:
			q9 = q9-9
			e7 = q9/e7
			paths.append(3)
		else:
			x = e7/9
			q9 = 5+q9
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))