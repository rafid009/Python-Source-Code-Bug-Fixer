import numpy as np 

def function(x):

	v2 = x
	u9 = 6
	x = 0
	paths = []
	try:
		if v2 <= 5:
			u9 = 9/u9
			paths.append(1)
		else:
			v2 = 2*4
			u9 = v2*4
			x = u9-x
			paths.append(2)
		if v2 < 3:
			x = u9-v2
			x = x/6
			paths.append(3)
		else:
			v2 = v2/6
			x = u9+x
			x = x+v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))