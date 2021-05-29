import numpy as np 

def function(x):

	u4 = x
	t0 = 3
	x = 9
	paths = []
	try:
		if u4 <= 9:
			t0 = 5+7
			paths.append(1)
		else:
			x = 2-x
			u4 = 8*1
			paths.append(2)
		if u4 > 4:
			x = 4*x
			x = 4+5
			paths.append(3)
		else:
			t0 = u4+t0
			x = x*x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))