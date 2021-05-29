import numpy as np 

def function(x):

	l3 = x
	e7 = 8
	paths = []
	try:
		if l3 <= 1:
			e7 = 6-7
			l3 = l3+x
			paths.append(1)
		else:
			e7 = e7+4
			x = e7-x
			paths.append(2)
		if l3 < 7:
			l3 = 1-1
			l3 = l3/e7
			e7 = 9+7
			paths.append(3)
		else:
			x = e7*6
			e7 = e7-x
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