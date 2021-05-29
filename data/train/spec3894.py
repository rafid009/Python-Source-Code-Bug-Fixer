import numpy as np 

def function(x):

	t2 = 5
	t7 = x
	x = x
	paths = []
	try:
		if t7 < 6:
			x = x/t2
			paths.append(1)
		else:
			x = t2*t2
			paths.append(2)
		if x >= 5:
			t7 = 5-t7
			x = x-0
			x = 0*8
			paths.append(3)
		else:
			t7 = t7/8
			t2 = t2+t2
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