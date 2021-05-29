import numpy as np 

def function(x):

	q6 = x
	o2 = 5
	paths = []
	try:
		if x > 7:
			x = 7*x
			paths.append(1)
		else:
			o2 = o2-0
			q6 = q6*8
			o2 = 9*q6
			paths.append(2)
		if q6 <= 8:
			q6 = x*1
			paths.append(3)
		else:
			o2 = o2/x
			x = x*9
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