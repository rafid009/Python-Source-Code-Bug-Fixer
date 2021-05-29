import numpy as np 

def function(x):

	a9 = 7
	q8 = 9
	paths = []
	try:
		if a9 < 1:
			a9 = a9-7
			q8 = q8-1
			q8 = q8/7
			paths.append(1)
		else:
			x = x+x
			q8 = x+q8
			paths.append(2)
		if a9 < 6:
			a9 = a9-5
			a9 = 4/a9
			a9 = q8+a9
			paths.append(3)
		else:
			a9 = a9/3
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		a9 = q8**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))