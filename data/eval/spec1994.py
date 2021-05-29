import numpy as np 

def function(x):

	q2 = x
	v2 = x
	paths = []
	try:
		if q2 > 3:
			x = x-x
			paths.append(1)
		else:
			v2 = x-5
			v2 = 6+9
			q2 = q2+q2
			paths.append(2)
		if v2 <= 2:
			v2 = x/q2
			q2 = q2+q2
			x = x-x
			paths.append(3)
		else:
			x = x-q2
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