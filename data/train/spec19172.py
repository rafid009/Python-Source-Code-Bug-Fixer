import numpy as np 

def function(x):

	e8 = 8
	u1 = x
	paths = []
	try:
		if x >= 0:
			u1 = 8/u1
			x = e8*7
			paths.append(1)
		else:
			x = x*0
			e8 = 1+e8
			paths.append(2)
		if u1 >= 4:
			x = x/u1
			e8 = e8-1
			paths.append(3)
		else:
			e8 = 9/8
			x = 7+x
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