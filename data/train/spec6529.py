import numpy as np 

def function(x):

	l3 = x
	l7 = 5
	paths = []
	try:
		if l7 >= 9:
			x = x*3
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if x > 5:
			x = x+l7
			paths.append(3)
		else:
			x = x+l7
			l3 = 7/1
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