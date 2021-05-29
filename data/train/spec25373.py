import numpy as np 

def function(x):

	t7 = x
	e8 = x
	paths = []
	try:
		if t7 >= 7:
			x = x/1
			e8 = e8-5
			t7 = t7+t7
			paths.append(1)
		else:
			t7 = 5+t7
			t7 = 7*2
			paths.append(2)
		if x < 9:
			t7 = 8*t7
			e8 = e8/x
			t7 = e8*x
			paths.append(3)
		else:
			x = t7+0
			t7 = t7/x
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