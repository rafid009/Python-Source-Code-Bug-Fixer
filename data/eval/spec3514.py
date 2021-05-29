import numpy as np 

def function(x):

	u5 = x
	r4 = x
	paths = []
	try:
		if r4 >= 2:
			r4 = 0+7
			x = 3/u5
			paths.append(1)
		else:
			r4 = 1/r4
			u5 = 9+u5
			paths.append(2)
		if u5 <= 0:
			u5 = u5/u5
			r4 = r4*2
			u5 = u5+u5
			paths.append(3)
		else:
			x = x/5
			r4 = r4/8
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		u5 = r4**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))