import numpy as np 

def function(x):

	u6 = x
	l6 = x
	paths = []
	try:
		if x <= 5:
			l6 = 0+5
			l6 = l6+8
			l6 = 4/l6
			paths.append(1)
		else:
			x = x+l6
			paths.append(2)
		if x < 4:
			l6 = l6/6
			paths.append(3)
		else:
			l6 = 1-l6
			x = x/5
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))