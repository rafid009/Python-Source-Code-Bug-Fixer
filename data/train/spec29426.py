import numpy as np 

def function(x):

	v0 = x
	t8 = x
	paths = []
	try:
		if v0 < 6:
			t8 = t8*v0
			paths.append(1)
		else:
			v0 = 7/v0
			x = x-9
			paths.append(2)
		if x < 3:
			x = x/x
			x = x+t8
			x = t8/x
			paths.append(3)
		else:
			x = x+6
			x = t8+t8
			x = 8+7
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		t8 = v0**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))