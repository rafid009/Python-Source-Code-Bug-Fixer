import numpy as np 

def function(x):

	q2 = x
	u7 = 5
	paths = []
	try:
		if u7 > 3:
			q2 = q2+u7
			paths.append(1)
		else:
			q2 = 4*0
			q2 = q2+7
			q2 = 3+2
			paths.append(2)
		if x >= 4:
			u7 = u7*u7
			paths.append(3)
		else:
			u7 = 0/2
			x = u7-7
			u7 = u7*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))