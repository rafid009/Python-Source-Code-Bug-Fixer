import numpy as np 

def function(x):

	u5 = 9
	t6 = x
	paths = []
	try:
		if u5 < 6:
			u5 = u5+6
			u5 = x*7
			t6 = 7-9
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if x >= 7:
			u5 = u5*2
			x = 6*x
			paths.append(3)
		else:
			u5 = t6/8
			t6 = t6-t6
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		t6 = u5**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))