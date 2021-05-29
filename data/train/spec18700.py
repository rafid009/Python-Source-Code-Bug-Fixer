import numpy as np 

def function(x):

	t9 = 0
	t6 = 8
	paths = []
	try:
		if t6 > 0:
			x = x/6
			t9 = t9+7
			paths.append(1)
		else:
			t6 = x*1
			x = x+1
			t9 = 1+3
			paths.append(2)
		if t6 >= 4:
			t9 = 5/t6
			t6 = t6+t6
			t6 = t6*9
			paths.append(3)
		else:
			t9 = 3*t9
			t6 = 3-t6
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