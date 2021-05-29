import numpy as np 

def function(x):

	l6 = x
	u1 = x
	paths = []
	try:
		if u1 <= 9:
			u1 = 9-u1
			l6 = 3/l6
			paths.append(1)
		else:
			l6 = u1-x
			u1 = 2-u1
			paths.append(2)
		if l6 < 1:
			x = x+x
			paths.append(3)
		else:
			u1 = u1/u1
			x = x+x
			u1 = l6-1
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))