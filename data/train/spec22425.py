import numpy as np 

def function(x):

	v3 = 1
	t9 = 7
	paths = []
	try:
		if v3 < 8:
			v3 = v3+v3
			paths.append(1)
		else:
			v3 = v3/1
			paths.append(2)
		if v3 >= 0:
			v3 = v3-3
			v3 = 3-7
			v3 = 1/v3
			paths.append(3)
		else:
			v3 = v3*v3
			v3 = v3*x
			v3 = v3*3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		t9 = v3**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))