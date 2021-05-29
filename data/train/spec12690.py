import numpy as np 

def function(x):

	q9 = x
	u5 = x
	paths = []
	try:
		if x < 6:
			u5 = u5/2
			q9 = q9+4
			u5 = 2*u5
			paths.append(1)
		else:
			q9 = q9+6
			u5 = 7-u5
			paths.append(2)
		if q9 <= 2:
			x = x*4
			q9 = u5+q9
			x = x+7
			paths.append(3)
		else:
			u5 = 7*7
			q9 = u5+q9
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))