import numpy as np 

def function(x):

	l5 = 4
	u7 = x
	paths = []
	try:
		if x <= 0:
			u7 = u7+u7
			paths.append(1)
		else:
			u7 = u7+1
			paths.append(2)
		if u7 >= 7:
			l5 = 4/l5
			u7 = 5*2
			u7 = 9-u7
			paths.append(3)
		else:
			l5 = u7-6
			l5 = 1+l5
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))