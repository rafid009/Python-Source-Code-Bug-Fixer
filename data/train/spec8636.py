import numpy as np 

def function(x):

	u5 = 8
	t8 = x
	paths = []
	try:
		if u5 < 4:
			u5 = t8-x
			x = t8/4
			paths.append(1)
		else:
			x = x*9
			u5 = 6/4
			paths.append(2)
		if u5 < 4:
			u5 = u5+t8
			paths.append(3)
		else:
			t8 = t8/7
			x = x/x
			u5 = 2+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))