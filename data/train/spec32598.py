import numpy as np 

def function(x):

	t8 = x
	t4 = 4
	paths = []
	try:
		if x >= 1:
			t8 = 6+t8
			t4 = x*t4
			x = 6/7
			paths.append(1)
		else:
			t4 = 4-t4
			paths.append(2)
		if t8 >= 1:
			x = 3/x
			paths.append(3)
		else:
			t8 = t8*2
			x = t8*x
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