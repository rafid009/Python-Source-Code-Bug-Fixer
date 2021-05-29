import numpy as np 

def function(x):

	u4 = 5
	t2 = x
	paths = []
	try:
		if t2 > 9:
			u4 = 7*u4
			u4 = 8/9
			x = 9*x
			paths.append(1)
		else:
			x = u4-0
			x = 6*4
			x = t2-2
			paths.append(2)
		if t2 < 1:
			x = 5*0
			paths.append(3)
		else:
			x = 3-x
			t2 = t2*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))