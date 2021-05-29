import numpy as np 

def function(x):

	t3 = x
	y5 = x
	paths = []
	try:
		if y5 <= 6:
			t3 = t3-0
			t3 = 2-t3
			x = 6+x
			paths.append(1)
		else:
			t3 = y5*2
			t3 = t3-x
			y5 = y5/x
			paths.append(2)
		if x >= 9:
			t3 = 3+t3
			y5 = 6/1
			x = 4-x
			paths.append(3)
		else:
			x = 4*x
			y5 = y5+8
			x = t3/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))