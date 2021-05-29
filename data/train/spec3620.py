import numpy as np 

def function(x):

	l1 = x
	u1 = 3
	paths = []
	try:
		if x > 5:
			x = 3-x
			l1 = l1*2
			x = x/u1
			paths.append(1)
		else:
			u1 = u1+4
			l1 = l1/4
			x = x*x
			paths.append(2)
		if x >= 4:
			u1 = l1*6
			paths.append(3)
		else:
			u1 = u1-1
			l1 = 5/l1
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		u1 = l1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))