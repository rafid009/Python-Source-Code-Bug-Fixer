import numpy as np 

def function(x):

	l6 = 5
	l1 = x
	paths = []
	try:
		if x < 2:
			x = 8*x
			x = x-l6
			paths.append(1)
		else:
			x = 3/6
			paths.append(2)
		if x > 7:
			l6 = 8+8
			l1 = 6-0
			paths.append(3)
		else:
			x = x*l1
			x = x*2
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l6 = l1**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))