import numpy as np 

def function(x):

	l1 = 8
	u5 = 8
	paths = []
	try:
		if u5 < 5:
			l1 = 5-3
			paths.append(1)
		else:
			l1 = 3*l1
			paths.append(2)
		if x > 4:
			x = 2*x
			u5 = u5-l1
			l1 = u5*7
			paths.append(3)
		else:
			u5 = l1-u5
			l1 = 8*5
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))