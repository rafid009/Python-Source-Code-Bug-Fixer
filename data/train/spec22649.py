import numpy as np 

def function(x):

	t5 = 2
	r8 = x
	paths = []
	try:
		if r8 > 6:
			t5 = 5-6
			paths.append(1)
		else:
			r8 = 8*5
			paths.append(2)
		if t5 < 8:
			x = 2-x
			t5 = 5/8
			paths.append(3)
		else:
			r8 = 3/9
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))