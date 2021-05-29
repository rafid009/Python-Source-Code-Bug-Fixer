import numpy as np 

def function(x):

	u6 = 2
	u1 = x
	x = 9
	paths = []
	try:
		if x > 3:
			x = x/x
			u6 = u1+u1
			paths.append(1)
		else:
			u1 = 7*u1
			u1 = u1-3
			u6 = u6+4
			paths.append(2)
		if u6 < 7:
			u1 = 3+u1
			paths.append(3)
		else:
			u1 = u1/u1
			u1 = u1*3
			u1 = u1*8
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u1 = u6**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))