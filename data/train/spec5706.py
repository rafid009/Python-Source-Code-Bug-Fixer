import numpy as np 

def function(x):

	l6 = 4
	u1 = x
	paths = []
	try:
		if u1 >= 7:
			u1 = u1+2
			u1 = u1-u1
			l6 = l6*3
			paths.append(1)
		else:
			x = x*l6
			l6 = 6-l6
			paths.append(2)
		if u1 > 6:
			x = 8/5
			paths.append(3)
		else:
			x = 6*x
			l6 = l6*4
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		l6 = u1**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))