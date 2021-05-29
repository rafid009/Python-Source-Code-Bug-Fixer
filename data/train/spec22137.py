import numpy as np 

def function(x):

	d8 = x
	t8 = x
	paths = []
	try:
		if d8 >= 6:
			t8 = x+t8
			x = x+3
			paths.append(1)
		else:
			x = 0+x
			x = x/3
			paths.append(2)
		if d8 < 0:
			t8 = x*6
			paths.append(3)
		else:
			t8 = 7/5
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		t8 = d8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))