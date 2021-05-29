import numpy as np 

def function(x):

	u1 = x
	f8 = 1
	paths = []
	try:
		if x > 9:
			u1 = u1+0
			x = f8/4
			u1 = 1-9
			paths.append(1)
		else:
			f8 = 1+5
			f8 = f8+8
			paths.append(2)
		if u1 <= 0:
			f8 = f8-2
			u1 = u1+f8
			paths.append(3)
		else:
			u1 = u1/x
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))