import numpy as np 

def function(x):

	t4 = x
	g6 = 9
	x = 7
	paths = []
	try:
		if t4 >= 8:
			g6 = 3+t4
			paths.append(1)
		else:
			x = 5/7
			paths.append(2)
		if x > 5:
			t4 = x-t4
			paths.append(3)
		else:
			g6 = t4*5
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		t4 = g6**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))