import numpy as np 

def function(x):

	u9 = 8
	l0 = x
	paths = []
	try:
		if u9 > 4:
			x = x/x
			u9 = 2/u9
			paths.append(1)
		else:
			u9 = u9-1
			x = x*6
			u9 = l0*u9
			paths.append(2)
		if l0 <= 6:
			x = 0*6
			u9 = u9/u9
			u9 = u9/u9
			paths.append(3)
		else:
			u9 = u9/6
			x = x/4
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		u9 = l0**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))