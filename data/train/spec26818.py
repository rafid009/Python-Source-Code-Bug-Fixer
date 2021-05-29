import numpy as np 

def function(x):

	u3 = x
	q7 = 4
	paths = []
	try:
		if q7 < 7:
			q7 = 4-q7
			x = 3-x
			q7 = u3*u3
			paths.append(1)
		else:
			u3 = u3+6
			paths.append(2)
		if u3 < 2:
			x = x/u3
			x = x/1
			q7 = q7/x
			paths.append(3)
		else:
			q7 = 7+q7
			x = x/7
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		q7 = u3**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))