import numpy as np 

def function(x):

	t6 = 2
	r8 = x
	x = x
	paths = []
	try:
		if t6 <= 7:
			r8 = x-0
			x = r8-x
			paths.append(1)
		else:
			x = 8/r8
			t6 = t6+4
			paths.append(2)
		if t6 > 8:
			t6 = 4/t6
			x = 9*x
			r8 = r8/x
			paths.append(3)
		else:
			r8 = r8/5
			x = 1*x
			x = x+3
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))