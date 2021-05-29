import numpy as np 

def function(x):

	b0 = x
	t7 = x
	paths = []
	try:
		if t7 < 5:
			t7 = 9-t7
			t7 = t7*t7
			paths.append(1)
		else:
			x = 0*7
			b0 = b0+4
			x = 5-x
			paths.append(2)
		if t7 > 8:
			t7 = 3*t7
			paths.append(3)
		else:
			t7 = 0/t7
			x = t7/4
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))