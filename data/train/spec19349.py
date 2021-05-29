import numpy as np 

def function(x):

	x8 = 8
	t3 = x
	paths = []
	try:
		if x > 5:
			x = 7/x
			t3 = 0/5
			paths.append(1)
		else:
			t3 = t3+0
			paths.append(2)
		if x8 > 1:
			x8 = 2+7
			x8 = x8/x8
			t3 = t3+6
			paths.append(3)
		else:
			t3 = 1/t3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x8 = t3**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))