import numpy as np 

def function(x):

	v6 = x
	l7 = 9
	paths = []
	try:
		if l7 < 0:
			l7 = v6/l7
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if v6 > 5:
			v6 = v6*5
			paths.append(3)
		else:
			x = x/8
			v6 = v6/2
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