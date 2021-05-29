import numpy as np 

def function(x):

	v9 = 1
	t4 = x
	paths = []
	try:
		if x < 7:
			x = v9-8
			t4 = t4+x
			t4 = t4/1
			paths.append(1)
		else:
			t4 = t4*5
			t4 = 7/t4
			t4 = v9+0
			paths.append(2)
		if v9 >= 6:
			t4 = t4-9
			paths.append(3)
		else:
			t4 = t4*5
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		v9 = t4**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))