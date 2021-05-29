import numpy as np 

def function(x):

	q6 = x
	l6 = x
	paths = []
	try:
		if l6 < 0:
			x = x/8
			q6 = q6*1
			paths.append(1)
		else:
			x = q6*5
			paths.append(2)
		if l6 > 0:
			l6 = l6-6
			q6 = q6*8
			l6 = q6/l6
			paths.append(3)
		else:
			l6 = 8/1
			q6 = q6+l6
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