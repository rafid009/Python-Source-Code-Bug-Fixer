import numpy as np 

def function(x):

	t8 = x
	v3 = 3
	paths = []
	try:
		if x >= 3:
			v3 = v3+8
			x = x-0
			x = 9/x
			paths.append(1)
		else:
			v3 = 5+v3
			paths.append(2)
		if x > 3:
			x = 6*9
			v3 = x-v3
			paths.append(3)
		else:
			v3 = x/3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		t8 = v3**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))