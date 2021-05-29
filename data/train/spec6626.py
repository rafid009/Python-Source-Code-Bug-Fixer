import numpy as np 

def function(x):

	t4 = x
	t7 = 1
	paths = []
	try:
		if t4 <= 4:
			t4 = 0*x
			x = 0+x
			paths.append(1)
		else:
			t4 = t7+t4
			t7 = 7-t7
			x = x*3
			paths.append(2)
		if t4 > 4:
			t7 = 5+0
			paths.append(3)
		else:
			t7 = t7-3
			x = x-t7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))