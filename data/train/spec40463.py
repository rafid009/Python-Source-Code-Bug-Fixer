import numpy as np 

def function(x):

	t3 = x
	a7 = x
	paths = []
	try:
		if a7 < 8:
			x = x-2
			paths.append(1)
		else:
			x = 0*1
			t3 = 5/t3
			paths.append(2)
		if t3 < 9:
			a7 = a7+0
			x = 7-9
			paths.append(3)
		else:
			t3 = t3*t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))