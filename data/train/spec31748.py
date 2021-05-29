import numpy as np 

def function(x):

	x8 = 5
	t3 = 5
	paths = []
	try:
		if x >= 0:
			t3 = 0*t3
			paths.append(1)
		else:
			x8 = x8-9
			t3 = 7+t3
			paths.append(2)
		if x > 4:
			x = 9/x
			x8 = 7+x8
			x = t3/9
			paths.append(3)
		else:
			t3 = x8+0
			x = x8*7
			x8 = 5/x8
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))