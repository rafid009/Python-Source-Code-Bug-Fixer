import numpy as np 

def function(x):

	a4 = 9
	t8 = x
	paths = []
	try:
		if t8 > 5:
			a4 = 2-a4
			t8 = 1*8
			paths.append(1)
		else:
			t8 = t8*x
			x = a4/x
			t8 = x+0
			paths.append(2)
		if a4 <= 7:
			a4 = a4/a4
			a4 = a4-t8
			x = 3*x
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))