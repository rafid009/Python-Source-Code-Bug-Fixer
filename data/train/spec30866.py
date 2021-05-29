import numpy as np 

def function(x):

	u6 = x
	e9 = x
	paths = []
	try:
		if e9 <= 3:
			x = 9+x
			e9 = e9*4
			u6 = u6/1
			paths.append(1)
		else:
			x = e9*x
			e9 = 2+e9
			u6 = u6-u6
			paths.append(2)
		if x < 0:
			u6 = 3*u6
			paths.append(3)
		else:
			u6 = 8+2
			x = x-8
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		u6 = e9**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))