import numpy as np 

def function(x):

	v8 = 4
	u1 = x
	x = 8
	paths = []
	try:
		if x > 6:
			x = 6*u1
			u1 = u1-6
			u1 = 6*x
			paths.append(1)
		else:
			x = v8/8
			u1 = u1+6
			paths.append(2)
		if u1 < 4:
			v8 = v8-v8
			paths.append(3)
		else:
			x = x*v8
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))