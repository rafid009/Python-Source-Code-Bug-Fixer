import numpy as np 

def function(x):

	u9 = 3
	o3 = x
	paths = []
	try:
		if o3 <= 7:
			x = o3/1
			x = 5-x
			paths.append(1)
		else:
			u9 = 0/u9
			paths.append(2)
		if o3 < 1:
			x = 8/u9
			o3 = 6+2
			paths.append(3)
		else:
			u9 = u9-2
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))