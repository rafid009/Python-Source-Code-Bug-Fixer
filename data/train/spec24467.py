import numpy as np 

def function(x):

	t4 = x
	x0 = x
	paths = []
	try:
		if t4 >= 5:
			t4 = 3/t4
			x = x0*t4
			paths.append(1)
		else:
			x0 = x0+9
			paths.append(2)
		if x < 5:
			x = 4*7
			x0 = t4/8
			paths.append(3)
		else:
			t4 = t4/3
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))