import numpy as np 

def function(x):

	a2 = x
	u5 = 9
	paths = []
	try:
		if x <= 1:
			u5 = 5-u5
			paths.append(1)
		else:
			a2 = 5+a2
			paths.append(2)
		if x > 6:
			u5 = x+1
			u5 = 5*u5
			paths.append(3)
		else:
			a2 = a2+3
			x = x*u5
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