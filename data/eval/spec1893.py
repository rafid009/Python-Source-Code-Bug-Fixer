import numpy as np 

def function(x):

	k2 = 7
	q6 = x
	paths = []
	try:
		if k2 >= 2:
			k2 = 1*4
			q6 = q6+0
			paths.append(1)
		else:
			q6 = q6+4
			x = x+5
			paths.append(2)
		if k2 > 4:
			x = x+2
			k2 = 2*k2
			paths.append(3)
		else:
			k2 = 8*q6
			k2 = 4*k2
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))