import numpy as np 

def function(x):

	u1 = x
	r1 = x
	x = x
	paths = []
	try:
		if x >= 9:
			u1 = u1*8
			x = x*1
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if x > 3:
			x = 4/6
			paths.append(3)
		else:
			x = r1+9
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))