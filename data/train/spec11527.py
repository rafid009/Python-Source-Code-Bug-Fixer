import numpy as np 

def function(x):

	y1 = x
	t6 = x
	paths = []
	try:
		if x > 7:
			y1 = x*t6
			x = t6+y1
			t6 = x*t6
			paths.append(1)
		else:
			y1 = y1-x
			t6 = 8-x
			t6 = y1/5
			paths.append(2)
		if y1 <= 2:
			y1 = y1*1
			paths.append(3)
		else:
			y1 = 2+t6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))