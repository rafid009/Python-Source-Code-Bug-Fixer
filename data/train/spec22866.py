import numpy as np 

def function(x):

	u5 = 2
	l9 = 3
	paths = []
	try:
		if l9 > 5:
			x = x-7
			paths.append(1)
		else:
			u5 = u5*x
			x = x/4
			x = 7+u5
			paths.append(2)
		if u5 >= 4:
			x = x/7
			u5 = 2+u5
			x = 2-x
			paths.append(3)
		else:
			u5 = u5+u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))