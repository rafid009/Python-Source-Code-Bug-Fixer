import numpy as np 

def function(x):

	q2 = 4
	u1 = 8
	paths = []
	try:
		if q2 <= 0:
			q2 = q2*0
			u1 = 8*u1
			q2 = 7/q2
			paths.append(1)
		else:
			u1 = u1-2
			paths.append(2)
		if u1 >= 7:
			u1 = u1+7
			x = x*3
			u1 = u1-5
			paths.append(3)
		else:
			u1 = q2/u1
			u1 = 4*x
			q2 = 2-2
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))