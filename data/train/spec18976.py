import numpy as np 

def function(x):

	t5 = 0
	t6 = x
	x = 4
	paths = []
	try:
		if t6 > 2:
			x = 0*5
			t6 = 0*t6
			t5 = 8+t5
			paths.append(1)
		else:
			t5 = 9+t6
			paths.append(2)
		if t5 > 2:
			t6 = t6*4
			t6 = t6+x
			paths.append(3)
		else:
			t6 = 6*9
			t6 = t6-t6
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))