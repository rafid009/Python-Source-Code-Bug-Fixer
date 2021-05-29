import numpy as np 

def function(x):

	u9 = x
	l6 = x
	paths = []
	try:
		if l6 > 1:
			x = x/3
			paths.append(1)
		else:
			x = 2+l6
			l6 = l6*l6
			paths.append(2)
		if x < 3:
			x = 7*x
			u9 = x+2
			paths.append(3)
		else:
			u9 = u9-u9
			u9 = 3-u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		l6 = u9**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))