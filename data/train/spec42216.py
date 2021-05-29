import numpy as np 

def function(x):

	r3 = 5
	t7 = x
	paths = []
	try:
		if r3 < 0:
			x = x/x
			r3 = 5/4
			paths.append(1)
		else:
			r3 = 3*7
			r3 = t7/8
			paths.append(2)
		if x <= 8:
			r3 = 6*r3
			t7 = t7+8
			paths.append(3)
		else:
			t7 = t7+7
			t7 = t7/t7
			r3 = r3*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))