import numpy as np 

def function(x):

	t7 = x
	a5 = 9
	paths = []
	try:
		if t7 <= 9:
			t7 = a5+t7
			a5 = 9*x
			paths.append(1)
		else:
			t7 = a5+2
			t7 = 2+3
			a5 = a5*t7
			paths.append(2)
		if t7 < 4:
			x = 4+x
			t7 = t7-t7
			paths.append(3)
		else:
			a5 = x-x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))