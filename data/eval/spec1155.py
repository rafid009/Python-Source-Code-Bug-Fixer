import numpy as np 

def function(x):

	d7 = x
	u6 = x
	paths = []
	try:
		if u6 >= 8:
			u6 = 9+u6
			paths.append(1)
		else:
			u6 = x-2
			x = x-1
			paths.append(2)
		if u6 <= 9:
			x = 9+7
			paths.append(3)
		else:
			u6 = 5+x
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		d7 = u6**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))