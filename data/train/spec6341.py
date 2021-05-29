import numpy as np 

def function(x):

	v3 = 9
	t8 = 8
	paths = []
	try:
		if x <= 1:
			t8 = t8-7
			x = x+x
			t8 = 2/t8
			paths.append(1)
		else:
			v3 = t8-v3
			v3 = v3*5
			paths.append(2)
		if x <= 3:
			t8 = t8/6
			x = x/4
			paths.append(3)
		else:
			x = x+8
			v3 = v3/7
			v3 = x+1
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