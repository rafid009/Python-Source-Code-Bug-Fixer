import numpy as np 

def function(x):

	q2 = 8
	v3 = 6
	paths = []
	try:
		if q2 < 0:
			x = x*q2
			paths.append(1)
		else:
			v3 = 1+v3
			v3 = 4-v3
			x = 9*x
			paths.append(2)
		if x < 6:
			q2 = 4-q2
			v3 = 7-0
			x = x/1
			paths.append(3)
		else:
			q2 = 6-v3
			v3 = v3-q2
			q2 = 3+9
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		v3 = q2**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))