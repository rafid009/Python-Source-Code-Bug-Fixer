import numpy as np 

def function(x):

	q6 = x
	v5 = x
	paths = []
	try:
		if q6 > 4:
			q6 = 8+q6
			x = x+3
			v5 = 6-v5
			paths.append(1)
		else:
			v5 = x/3
			x = x*3
			q6 = 0-4
			paths.append(2)
		if x <= 9:
			x = 0*x
			paths.append(3)
		else:
			v5 = 7/8
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