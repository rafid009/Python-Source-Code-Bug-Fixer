import numpy as np 

def function(x):

	u3 = x
	t9 = 0
	paths = []
	try:
		if t9 < 4:
			x = x+u3
			x = 7-u3
			paths.append(1)
		else:
			x = 5/x
			t9 = 5*t9
			paths.append(2)
		if u3 >= 5:
			u3 = 3-8
			x = 2*x
			paths.append(3)
		else:
			x = 9/x
			u3 = 7+u3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))