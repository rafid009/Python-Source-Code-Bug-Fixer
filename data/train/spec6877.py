import numpy as np 

def function(x):

	t8 = x
	u3 = x
	paths = []
	try:
		if t8 >= 6:
			t8 = 7*t8
			t8 = t8*9
			paths.append(1)
		else:
			t8 = 0*4
			t8 = t8-t8
			x = x/4
			paths.append(2)
		if x > 7:
			x = 2-6
			paths.append(3)
		else:
			t8 = 7*x
			x = 3*x
			t8 = 3/t8
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))