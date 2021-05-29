import numpy as np 

def function(x):

	x5 = x
	l1 = 6
	paths = []
	try:
		if x5 > 8:
			x5 = 5/6
			l1 = 8/l1
			l1 = l1-x
			paths.append(1)
		else:
			l1 = l1+1
			x5 = x5-5
			l1 = 3-l1
			paths.append(2)
		if l1 < 9:
			l1 = l1*3
			paths.append(3)
		else:
			x5 = x5+5
			x5 = x5+l1
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