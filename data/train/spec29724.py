import numpy as np 

def function(x):

	u5 = 4
	l1 = 7
	paths = []
	try:
		if l1 <= 4:
			x = 8+x
			u5 = u5-l1
			paths.append(1)
		else:
			u5 = u5-3
			u5 = u5*x
			u5 = l1-u5
			paths.append(2)
		if l1 < 0:
			x = l1+7
			l1 = l1-x
			u5 = u5-0
			paths.append(3)
		else:
			u5 = u5/x
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))