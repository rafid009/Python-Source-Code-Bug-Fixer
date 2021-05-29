import numpy as np 

def function(x):

	e1 = x
	q1 = x
	paths = []
	try:
		if q1 <= 7:
			e1 = x+e1
			paths.append(1)
		else:
			q1 = 7+q1
			q1 = q1-e1
			x = x/4
			paths.append(2)
		if e1 >= 6:
			x = x-9
			x = x+0
			q1 = 5*1
			paths.append(3)
		else:
			q1 = 8+0
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		q1 = e1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))