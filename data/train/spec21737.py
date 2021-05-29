import numpy as np 

def function(x):

	l6 = x
	t4 = 3
	paths = []
	try:
		if t4 >= 6:
			t4 = l6/8
			paths.append(1)
		else:
			t4 = 3*0
			t4 = t4+3
			paths.append(2)
		if x < 9:
			t4 = t4-6
			paths.append(3)
		else:
			t4 = t4+t4
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))