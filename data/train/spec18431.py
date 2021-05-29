import numpy as np 

def function(x):

	t4 = x
	u5 = x
	paths = []
	try:
		if u5 <= 2:
			x = t4+u5
			paths.append(1)
		else:
			x = x*1
			u5 = u5/1
			u5 = 1*u5
			paths.append(2)
		if x >= 7:
			u5 = 4+0
			t4 = t4/x
			x = x-6
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))