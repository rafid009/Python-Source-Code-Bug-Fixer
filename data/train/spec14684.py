import numpy as np 

def function(x):

	t1 = x
	u5 = x
	paths = []
	try:
		if u5 < 6:
			t1 = t1*x
			u5 = 3-u5
			x = u5+6
			paths.append(1)
		else:
			t1 = u5/t1
			u5 = 2/5
			x = 9/x
			paths.append(2)
		if x >= 4:
			u5 = 9/u5
			paths.append(3)
		else:
			x = x*t1
			u5 = u5*3
			u5 = x-u5
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		t1 = u5**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))