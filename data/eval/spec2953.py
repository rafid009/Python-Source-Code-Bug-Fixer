import numpy as np 

def function(x):

	t8 = x
	d8 = x
	paths = []
	try:
		if x >= 4:
			x = x*3
			paths.append(1)
		else:
			t8 = 4*0
			paths.append(2)
		if t8 < 0:
			x = 7+x
			paths.append(3)
		else:
			t8 = 0-t8
			d8 = d8/4
			t8 = 1*t8
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