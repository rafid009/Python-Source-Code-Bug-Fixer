import numpy as np 

def function(x):

	q1 = x
	u4 = x
	paths = []
	try:
		if x < 8:
			u4 = q1+u4
			x = u4+4
			paths.append(1)
		else:
			x = 0/x
			x = 5+x
			paths.append(2)
		if x <= 8:
			u4 = u4*8
			x = q1*x
			x = x+9
			paths.append(3)
		else:
			x = 2+x
			u4 = u4*q1
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))