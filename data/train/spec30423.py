import numpy as np 

def function(x):

	u7 = x
	q5 = x
	paths = []
	try:
		if x >= 9:
			u7 = 4*u7
			q5 = 3-u7
			paths.append(1)
		else:
			x = 9+5
			u7 = 0*u7
			paths.append(2)
		if u7 < 0:
			q5 = 0*8
			u7 = u7*9
			paths.append(3)
		else:
			q5 = q5+q5
			u7 = u7-7
			q5 = 5*5
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))