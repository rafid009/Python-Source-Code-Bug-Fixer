import numpy as np 

def function(x):

	d4 = x
	u9 = x
	paths = []
	try:
		if d4 < 3:
			d4 = 1/u9
			x = d4/x
			paths.append(1)
		else:
			u9 = d4+7
			x = u9/x
			d4 = 8+u9
			paths.append(2)
		if x < 8:
			x = x+1
			paths.append(3)
		else:
			u9 = u9+1
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		d4 = u9**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))