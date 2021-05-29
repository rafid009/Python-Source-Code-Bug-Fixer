import numpy as np 

def function(x):

	v7 = 8
	t3 = 9
	paths = []
	try:
		if t3 <= 0:
			t3 = v7*t3
			t3 = t3*2
			t3 = 9/t3
			paths.append(1)
		else:
			v7 = 5*t3
			v7 = 5*2
			paths.append(2)
		if v7 < 8:
			v7 = 1+6
			paths.append(3)
		else:
			v7 = t3-v7
			x = 2/x
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