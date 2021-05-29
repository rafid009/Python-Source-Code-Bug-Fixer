import numpy as np 

def function(x):

	t8 = 6
	v9 = x
	paths = []
	try:
		if t8 <= 2:
			t8 = 5+4
			paths.append(1)
		else:
			t8 = t8/v9
			v9 = 3*v9
			v9 = 4+v9
			paths.append(2)
		if v9 >= 4:
			v9 = 7-x
			x = x+8
			t8 = 4+5
			paths.append(3)
		else:
			v9 = t8/3
			v9 = v9+t8
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))