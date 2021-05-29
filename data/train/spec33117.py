import numpy as np 

def function(x):

	b8 = 6
	u1 = x
	x = x
	paths = []
	try:
		if u1 <= 5:
			x = x*x
			paths.append(1)
		else:
			x = 3/x
			b8 = 3+b8
			x = u1+x
			paths.append(2)
		if b8 < 6:
			x = u1/x
			u1 = b8/u1
			paths.append(3)
		else:
			u1 = 0+7
			u1 = x-u1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))