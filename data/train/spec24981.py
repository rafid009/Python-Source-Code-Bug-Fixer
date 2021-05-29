import numpy as np 

def function(x):

	q6 = 4
	u6 = x
	paths = []
	try:
		if x > 5:
			x = 8*7
			x = u6/6
			x = 9*x
			paths.append(1)
		else:
			u6 = u6+6
			q6 = q6-x
			paths.append(2)
		if u6 < 6:
			x = u6+q6
			q6 = 9/3
			paths.append(3)
		else:
			q6 = 5-q6
			u6 = x*u6
			q6 = x/9
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))