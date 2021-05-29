import numpy as np 

def function(x):

	l0 = x
	q6 = x
	paths = []
	try:
		if x > 9:
			l0 = l0*9
			paths.append(1)
		else:
			q6 = q6+2
			paths.append(2)
		if q6 < 4:
			l0 = l0+x
			q6 = q6/8
			x = q6-x
			paths.append(3)
		else:
			x = q6*5
			x = l0*4
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		l0 = q6**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))