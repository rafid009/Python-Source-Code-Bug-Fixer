import numpy as np 

def function(x):

	l0 = 2
	t8 = x
	paths = []
	try:
		if x <= 5:
			l0 = l0-l0
			x = 4*x
			paths.append(1)
		else:
			t8 = t8-6
			t8 = 0*t8
			t8 = 3*t8
			paths.append(2)
		if l0 <= 5:
			x = 4*5
			paths.append(3)
		else:
			t8 = 7+7
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))