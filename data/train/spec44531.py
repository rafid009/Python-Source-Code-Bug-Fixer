import numpy as np 

def function(x):

	q6 = 5
	u3 = 0
	paths = []
	try:
		if u3 <= 3:
			x = q6*q6
			q6 = 8/q6
			u3 = u3*u3
			paths.append(1)
		else:
			u3 = q6/7
			q6 = q6+8
			paths.append(2)
		if x >= 7:
			u3 = x+6
			u3 = 8/7
			q6 = q6-4
			paths.append(3)
		else:
			u3 = 3-u3
			u3 = 5-u3
			u3 = q6/1
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))