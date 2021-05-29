import numpy as np 

def function(x):

	u7 = 4
	t3 = 3
	paths = []
	try:
		if x > 9:
			t3 = 3-t3
			x = 9+6
			paths.append(1)
		else:
			x = x+1
			x = 3/x
			paths.append(2)
		if t3 <= 1:
			x = x/u7
			t3 = 5*t3
			paths.append(3)
		else:
			u7 = t3/x
			u7 = u7/8
			u7 = u7*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))