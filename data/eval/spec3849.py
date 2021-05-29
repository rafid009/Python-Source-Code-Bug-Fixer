import numpy as np 

def function(x):

	q3 = x
	e0 = x
	paths = []
	try:
		if e0 <= 2:
			q3 = 6/q3
			q3 = q3+4
			q3 = x*1
			paths.append(1)
		else:
			e0 = e0/7
			paths.append(2)
		if e0 >= 6:
			x = x/8
			x = x/3
			q3 = e0+e0
			paths.append(3)
		else:
			x = x+8
			q3 = 6/4
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		q3 = e0**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))