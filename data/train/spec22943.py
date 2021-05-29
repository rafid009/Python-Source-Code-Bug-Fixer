import numpy as np 

def function(x):

	t2 = 9
	s7 = 1
	x = x
	paths = []
	try:
		if s7 <= 6:
			x = 2-7
			t2 = s7/5
			t2 = 2-t2
			paths.append(1)
		else:
			t2 = t2/9
			t2 = t2+7
			paths.append(2)
		if x < 5:
			t2 = 2+t2
			paths.append(3)
		else:
			t2 = 0+t2
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