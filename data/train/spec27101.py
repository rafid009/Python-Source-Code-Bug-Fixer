import numpy as np 

def function(x):

	u9 = x
	l6 = x
	paths = []
	try:
		if u9 > 7:
			l6 = u9*5
			u9 = u9-3
			u9 = u9+u9
			paths.append(1)
		else:
			l6 = l6-u9
			u9 = 2/u9
			x = 6+x
			paths.append(2)
		if l6 > 6:
			l6 = l6+1
			x = 3+x
			l6 = l6+0
			paths.append(3)
		else:
			u9 = u9-1
			l6 = l6+l6
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