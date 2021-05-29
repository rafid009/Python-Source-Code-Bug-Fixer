import numpy as np 

def function(x):

	q7 = x
	l8 = x
	paths = []
	try:
		if l8 <= 7:
			x = 7-x
			x = 7*x
			x = 7*1
			paths.append(1)
		else:
			q7 = q7/2
			paths.append(2)
		if q7 > 7:
			x = x*7
			l8 = 5/l8
			x = 5+0
			paths.append(3)
		else:
			x = x/q7
			l8 = l8*1
			q7 = q7*2
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))