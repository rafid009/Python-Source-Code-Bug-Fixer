import numpy as np 

def function(x):

	l7 = 8
	a1 = x
	x = 7
	paths = []
	try:
		if a1 <= 0:
			l7 = l7-a1
			l7 = l7/9
			paths.append(1)
		else:
			a1 = a1*x
			l7 = 1-l7
			paths.append(2)
		if a1 < 7:
			x = a1*x
			paths.append(3)
		else:
			x = 7+9
			l7 = 1/l7
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))