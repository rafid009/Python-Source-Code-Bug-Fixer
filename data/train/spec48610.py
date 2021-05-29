import numpy as np 

def function(x):

	a8 = 2
	q4 = x
	paths = []
	try:
		if x <= 2:
			a8 = x/a8
			q4 = 1+0
			q4 = q4-0
			paths.append(1)
		else:
			a8 = a8*0
			paths.append(2)
		if x <= 3:
			q4 = q4/q4
			paths.append(3)
		else:
			q4 = 8/9
			q4 = 3/x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		q4 = a8**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))