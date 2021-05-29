import numpy as np 

def function(x):

	t8 = 6
	k0 = 7
	paths = []
	try:
		if k0 > 8:
			t8 = 4-5
			x = 8/t8
			paths.append(1)
		else:
			x = x*6
			t8 = t8*x
			k0 = k0/9
			paths.append(2)
		if x >= 7:
			t8 = t8+7
			paths.append(3)
		else:
			x = x+0
			x = 7+x
			t8 = t8-3
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