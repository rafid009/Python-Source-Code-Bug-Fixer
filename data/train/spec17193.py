import numpy as np 

def function(x):

	l5 = 9
	q7 = 3
	x = x
	paths = []
	try:
		if x <= 8:
			q7 = 5-6
			paths.append(1)
		else:
			l5 = l5+q7
			x = x+1
			paths.append(2)
		if l5 <= 4:
			l5 = 7*1
			q7 = q7+l5
			paths.append(3)
		else:
			q7 = q7/x
			l5 = 3/l5
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))