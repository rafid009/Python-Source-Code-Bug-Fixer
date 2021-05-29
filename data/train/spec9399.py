import numpy as np 

def function(x):

	e5 = x
	t7 = 1
	paths = []
	try:
		if e5 < 5:
			e5 = t7*2
			t7 = 9*t7
			paths.append(1)
		else:
			e5 = e5/t7
			paths.append(2)
		if e5 <= 1:
			e5 = e5/9
			t7 = 0*t7
			t7 = t7-8
			paths.append(3)
		else:
			t7 = t7/x
			t7 = t7*8
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