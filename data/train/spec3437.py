import numpy as np 

def function(x):

	v2 = x
	u5 = 3
	paths = []
	try:
		if v2 >= 7:
			u5 = 2*u5
			x = 7*x
			x = v2*6
			paths.append(1)
		else:
			u5 = u5*x
			u5 = u5*u5
			x = 5/7
			paths.append(2)
		if u5 >= 4:
			u5 = x*v2
			u5 = u5-6
			x = x-2
			paths.append(3)
		else:
			x = x/v2
			u5 = u5+6
			x = 0/5
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