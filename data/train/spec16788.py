import numpy as np 

def function(x):

	u0 = 9
	l3 = 4
	paths = []
	try:
		if x < 8:
			u0 = 5-x
			paths.append(1)
		else:
			u0 = u0-l3
			x = l3/9
			x = u0+5
			paths.append(2)
		if u0 > 9:
			u0 = u0+7
			l3 = 2/4
			paths.append(3)
		else:
			l3 = 0-9
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		l3 = u0**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))