import numpy as np 

def function(x):

	u9 = x
	q5 = 9
	x = 8
	paths = []
	try:
		if u9 <= 4:
			u9 = q5+u9
			paths.append(1)
		else:
			q5 = 3*q5
			paths.append(2)
		if x > 1:
			u9 = u9*q5
			paths.append(3)
		else:
			u9 = u9*4
			u9 = 0-u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		q5 = u9**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))