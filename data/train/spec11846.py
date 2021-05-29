import numpy as np 

def function(x):

	a6 = 2
	t8 = x
	paths = []
	try:
		if x <= 3:
			t8 = 1/9
			t8 = x+t8
			paths.append(1)
		else:
			a6 = 2*a6
			x = t8-4
			paths.append(2)
		if a6 > 5:
			t8 = 9+t8
			t8 = 8/1
			paths.append(3)
		else:
			a6 = a6*a6
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