import numpy as np 

def function(x):

	u6 = 8
	a1 = x
	paths = []
	try:
		if x >= 4:
			u6 = u6-x
			u6 = u6*8
			x = 7*x
			paths.append(1)
		else:
			x = x/8
			a1 = x*a1
			a1 = x*u6
			paths.append(2)
		if a1 > 5:
			a1 = a1-3
			u6 = u6+3
			paths.append(3)
		else:
			x = 3-0
			u6 = 3+6
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