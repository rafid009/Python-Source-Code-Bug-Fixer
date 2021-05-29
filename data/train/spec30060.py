import numpy as np 

def function(x):

	l1 = x
	u5 = 8
	paths = []
	try:
		if u5 >= 9:
			u5 = x/6
			x = x+4
			l1 = x-4
			paths.append(1)
		else:
			x = 3*6
			paths.append(2)
		if u5 >= 7:
			x = x+1
			paths.append(3)
		else:
			x = l1/6
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