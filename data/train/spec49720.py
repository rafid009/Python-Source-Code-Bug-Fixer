import numpy as np 

def function(x):

	a6 = x
	u9 = x
	paths = []
	try:
		if u9 <= 3:
			a6 = a6-6
			a6 = 2-3
			paths.append(1)
		else:
			a6 = 1*9
			paths.append(2)
		if x <= 7:
			x = 4/9
			u9 = u9/u9
			x = 4+x
			paths.append(3)
		else:
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		u9 = a6**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))