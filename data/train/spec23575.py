import numpy as np 

def function(x):

	t8 = x
	x8 = x
	paths = []
	try:
		if x8 <= 8:
			x8 = x+6
			t8 = 1-x
			x8 = x8*5
			paths.append(1)
		else:
			x = x*7
			x = x8-x
			paths.append(2)
		if x8 > 7:
			x = 4+t8
			t8 = t8/6
			paths.append(3)
		else:
			x8 = 8/4
			x = t8*x8
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x8 = t8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))