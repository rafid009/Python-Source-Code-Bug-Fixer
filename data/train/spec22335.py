import numpy as np 

def function(x):

	q3 = x
	v4 = x
	paths = []
	try:
		if q3 <= 0:
			x = x+q3
			q3 = q3*3
			q3 = q3/3
			paths.append(1)
		else:
			x = 5*v4
			q3 = 5*1
			paths.append(2)
		if q3 < 1:
			q3 = 8*4
			paths.append(3)
		else:
			q3 = 0/x
			v4 = x-8
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		q3 = v4**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))