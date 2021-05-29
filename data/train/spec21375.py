import numpy as np 

def function(x):

	t2 = x
	d9 = 3
	paths = []
	try:
		if t2 > 3:
			d9 = 8*1
			x = 6/7
			d9 = 6-9
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if t2 <= 5:
			x = 3/x
			x = 3*x
			d9 = d9+8
			paths.append(3)
		else:
			x = 7-0
			t2 = 1*t2
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))