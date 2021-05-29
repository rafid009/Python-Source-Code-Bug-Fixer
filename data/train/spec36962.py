import numpy as np 

def function(x):

	u3 = 0
	u4 = x
	paths = []
	try:
		if x <= 1:
			x = 8-9
			u3 = x+u3
			paths.append(1)
		else:
			u4 = u4+u3
			u4 = 1/u4
			x = x*4
			paths.append(2)
		if u3 > 3:
			u4 = 0/x
			paths.append(3)
		else:
			u3 = u4-1
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u4 = u3**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))