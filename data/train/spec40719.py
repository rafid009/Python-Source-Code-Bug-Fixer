import numpy as np 

def function(x):

	q8 = x
	e5 = x
	paths = []
	try:
		if x <= 8:
			q8 = x*4
			x = e5+x
			paths.append(1)
		else:
			x = 3/9
			x = 3-x
			paths.append(2)
		if q8 >= 6:
			e5 = e5*0
			e5 = 5*4
			x = x-7
			paths.append(3)
		else:
			q8 = 2/q8
			e5 = e5-7
			q8 = 5/e5
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))