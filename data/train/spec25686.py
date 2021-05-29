import numpy as np 

def function(x):

	t8 = 7
	o9 = x
	paths = []
	try:
		if t8 > 5:
			o9 = 9+x
			t8 = t8/t8
			o9 = o9+0
			paths.append(1)
		else:
			t8 = 8+t8
			paths.append(2)
		if t8 > 6:
			o9 = 0/9
			paths.append(3)
		else:
			o9 = 9/o9
			o9 = o9-2
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