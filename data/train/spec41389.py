import numpy as np 

def function(x):

	u9 = 5
	v0 = 5
	paths = []
	try:
		if u9 >= 9:
			v0 = 0+v0
			x = x/v0
			x = 3/x
			paths.append(1)
		else:
			u9 = u9/2
			v0 = x+v0
			paths.append(2)
		if u9 > 5:
			v0 = v0-v0
			x = u9/x
			paths.append(3)
		else:
			v0 = 5*v0
			u9 = u9/v0
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))