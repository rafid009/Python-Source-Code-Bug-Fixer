import numpy as np 

def function(x):

	l1 = x
	u6 = 3
	paths = []
	try:
		if x > 2:
			x = 2*x
			u6 = 0-8
			paths.append(1)
		else:
			l1 = 4/4
			u6 = u6-9
			paths.append(2)
		if u6 >= 8:
			l1 = u6/1
			l1 = u6+2
			l1 = 3/l1
			paths.append(3)
		else:
			l1 = l1-8
			x = x+4
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