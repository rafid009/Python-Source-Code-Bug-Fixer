import numpy as np 

def function(x):

	l2 = 7
	u9 = x
	paths = []
	try:
		if u9 <= 7:
			x = x+l2
			x = u9-0
			paths.append(1)
		else:
			u9 = 2-u9
			l2 = 0+u9
			u9 = 7*u9
			paths.append(2)
		if x <= 9:
			l2 = 1*2
			x = 3+l2
			paths.append(3)
		else:
			l2 = l2*9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))