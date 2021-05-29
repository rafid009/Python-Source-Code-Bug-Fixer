import numpy as np 

def function(x):

	t9 = x
	x0 = 4
	paths = []
	try:
		if x > 3:
			x = 8-x
			x0 = x0*7
			t9 = t9+1
			paths.append(1)
		else:
			x0 = 2-2
			paths.append(2)
		if t9 > 2:
			x = 8-5
			x0 = x0+t9
			t9 = 3*t9
			paths.append(3)
		else:
			t9 = 4+t9
			x = 8*1
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))