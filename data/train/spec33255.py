import numpy as np 

def function(x):

	q4 = 4
	a1 = x
	paths = []
	try:
		if x > 3:
			a1 = 7-q4
			q4 = q4/1
			paths.append(1)
		else:
			x = 4/8
			q4 = x+q4
			x = x/4
			paths.append(2)
		if a1 > 5:
			q4 = 6/5
			a1 = 8/a1
			paths.append(3)
		else:
			a1 = a1/3
			q4 = x-q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))