import numpy as np 

def function(x):

	u3 = x
	q4 = 3
	paths = []
	try:
		if q4 >= 0:
			q4 = q4-6
			q4 = q4/3
			x = 6*x
			paths.append(1)
		else:
			u3 = u3*u3
			paths.append(2)
		if q4 >= 1:
			x = x*0
			q4 = 1*q4
			paths.append(3)
		else:
			q4 = q4*7
			x = 6-x
			u3 = u3/4
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		q4 = u3**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))