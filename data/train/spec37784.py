import numpy as np 

def function(x):

	t9 = x
	g1 = x
	paths = []
	try:
		if g1 > 6:
			x = x*5
			paths.append(1)
		else:
			g1 = 1*g1
			paths.append(2)
		if t9 < 1:
			x = g1*6
			paths.append(3)
		else:
			t9 = 9+6
			t9 = t9-t9
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		t9 = g1**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))