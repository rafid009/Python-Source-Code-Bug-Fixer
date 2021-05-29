import numpy as np 

def function(x):

	l7 = 6
	q3 = 4
	paths = []
	try:
		if q3 <= 3:
			q3 = 2/3
			paths.append(1)
		else:
			l7 = q3/q3
			q3 = 7*0
			x = x/9
			paths.append(2)
		if q3 <= 4:
			q3 = l7*1
			paths.append(3)
		else:
			x = l7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))