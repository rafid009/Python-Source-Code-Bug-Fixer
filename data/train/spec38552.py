import numpy as np 

def function(x):

	u3 = x
	q1 = x
	paths = []
	try:
		if u3 <= 5:
			q1 = 6*7
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x <= 1:
			u3 = 8+u3
			q1 = 9/x
			paths.append(3)
		else:
			u3 = 0*x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		q1 = u3**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))