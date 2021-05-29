import numpy as np 

def function(x):

	u4 = 3
	l6 = x
	paths = []
	try:
		if l6 <= 5:
			x = x-0
			x = u4-x
			paths.append(1)
		else:
			x = 4/5
			u4 = u4+1
			paths.append(2)
		if u4 < 5:
			l6 = l6*7
			x = u4*x
			paths.append(3)
		else:
			l6 = l6+7
			u4 = u4/6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		u4 = l6**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))