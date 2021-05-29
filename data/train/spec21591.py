import numpy as np 

def function(x):

	u1 = x
	q2 = x
	paths = []
	try:
		if q2 >= 2:
			u1 = u1*u1
			u1 = u1/u1
			paths.append(1)
		else:
			u1 = 7*0
			x = 8+u1
			x = x-2
			paths.append(2)
		if u1 < 7:
			q2 = q2*3
			paths.append(3)
		else:
			q2 = q2+3
			q2 = 9+q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))