import numpy as np 

def function(x):

	u4 = x
	x2 = x
	paths = []
	try:
		if x2 >= 2:
			x2 = x*x2
			x = 7+9
			u4 = u4+1
			paths.append(1)
		else:
			x2 = 1/1
			x2 = x2*u4
			x2 = 9/9
			paths.append(2)
		if x <= 4:
			x = x*x
			x2 = 3+0
			paths.append(3)
		else:
			x2 = 8+u4
			u4 = u4/2
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x2 = u4**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))