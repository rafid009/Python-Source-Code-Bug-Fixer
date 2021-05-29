import numpy as np 

def function(x):

	u6 = x
	e6 = x
	paths = []
	try:
		if e6 >= 6:
			e6 = 7-e6
			paths.append(1)
		else:
			u6 = e6-0
			e6 = u6+4
			x = x*u6
			paths.append(2)
		if u6 >= 6:
			e6 = e6+3
			paths.append(3)
		else:
			u6 = u6+1
			x = x-e6
			e6 = e6/e6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		u6 = e6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))