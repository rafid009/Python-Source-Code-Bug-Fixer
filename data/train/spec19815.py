import numpy as np 

def function(x):

	u2 = x
	v1 = x
	x = 0
	paths = []
	try:
		if u2 >= 3:
			u2 = u2-v1
			paths.append(1)
		else:
			v1 = v1*8
			paths.append(2)
		if v1 > 8:
			x = 9/6
			paths.append(3)
		else:
			v1 = 7-v1
			x = u2+v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))