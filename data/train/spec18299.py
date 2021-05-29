import numpy as np 

def function(x):

	q7 = 8
	u3 = 0
	paths = []
	try:
		if u3 <= 3:
			x = x*q7
			x = 1*x
			paths.append(1)
		else:
			x = u3*5
			q7 = q7-q7
			q7 = q7+x
			paths.append(2)
		if u3 > 0:
			q7 = q7*q7
			paths.append(3)
		else:
			u3 = u3-5
			x = u3+x
			q7 = 9/5
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