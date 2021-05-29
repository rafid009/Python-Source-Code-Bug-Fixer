import numpy as np 

def function(x):

	u5 = x
	t1 = x
	paths = []
	try:
		if t1 <= 4:
			u5 = u5-5
			paths.append(1)
		else:
			t1 = t1*8
			t1 = t1+8
			u5 = t1*u5
			paths.append(2)
		if u5 >= 4:
			x = 6*4
			t1 = 3*7
			paths.append(3)
		else:
			x = x*u5
			t1 = x-t1
			x = 7/7
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