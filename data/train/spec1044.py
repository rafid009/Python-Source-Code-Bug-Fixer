import numpy as np 

def function(x):

	q6 = x
	u1 = x
	x = x
	paths = []
	try:
		if q6 < 7:
			x = x-x
			x = x*9
			paths.append(1)
		else:
			x = 5*u1
			x = x*9
			q6 = q6-3
			paths.append(2)
		if q6 < 6:
			x = 6-x
			x = 3*u1
			paths.append(3)
		else:
			u1 = 2+x
			u1 = u1+u1
			u1 = u1*1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		q6 = u1**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))