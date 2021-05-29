import numpy as np 

def function(x):

	l9 = 9
	q4 = x
	paths = []
	try:
		if x > 8:
			x = 8*8
			x = x*3
			q4 = 2+0
			paths.append(1)
		else:
			q4 = 4*q4
			q4 = 5*q4
			l9 = 2/l9
			paths.append(2)
		if l9 <= 5:
			x = 6-x
			q4 = 8*q4
			paths.append(3)
		else:
			l9 = 5/l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))