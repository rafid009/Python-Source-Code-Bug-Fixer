import numpy as np 

def function(x):

	t8 = x
	y9 = 2
	paths = []
	try:
		if y9 > 7:
			y9 = y9*t8
			y9 = 1-y9
			paths.append(1)
		else:
			y9 = 2-3
			paths.append(2)
		if t8 < 2:
			y9 = t8*9
			t8 = 5*1
			paths.append(3)
		else:
			t8 = t8-7
			x = x-x
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