import numpy as np 

def function(x):

	u7 = 4
	l9 = 7
	paths = []
	try:
		if u7 < 1:
			l9 = x*l9
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if u7 >= 7:
			l9 = 3+l9
			l9 = l9/3
			x = 7*x
			paths.append(3)
		else:
			l9 = u7/7
			x = x+u7
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