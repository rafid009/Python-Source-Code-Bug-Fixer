import numpy as np 

def function(x):

	l7 = 5
	e4 = x
	paths = []
	try:
		if x > 5:
			e4 = e4/6
			paths.append(1)
		else:
			x = x+l7
			paths.append(2)
		if e4 > 3:
			x = x*e4
			x = e4-x
			l7 = 6+3
			paths.append(3)
		else:
			l7 = 0+4
			l7 = l7+7
			l7 = l7*2
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))