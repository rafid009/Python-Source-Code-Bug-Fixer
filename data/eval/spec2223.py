import numpy as np 

def function(x):

	e1 = x
	u9 = x
	x = x
	paths = []
	try:
		if u9 >= 5:
			u9 = u9+x
			paths.append(1)
		else:
			u9 = u9*5
			u9 = u9+0
			paths.append(2)
		if u9 < 3:
			x = x*9
			u9 = u9*u9
			paths.append(3)
		else:
			e1 = e1/2
			u9 = x/x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		u9 = e1**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))