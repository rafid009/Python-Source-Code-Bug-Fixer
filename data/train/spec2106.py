import numpy as np 

def function(x):

	t4 = x
	u5 = 8
	paths = []
	try:
		if u5 < 4:
			t4 = 0+t4
			x = x/5
			paths.append(1)
		else:
			t4 = 2-t4
			paths.append(2)
		if t4 < 7:
			x = x*x
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))