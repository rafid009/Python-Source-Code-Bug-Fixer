import numpy as np 

def function(x):

	r3 = x
	t8 = 4
	paths = []
	try:
		if r3 > 2:
			r3 = r3*r3
			paths.append(1)
		else:
			t8 = 9-t8
			r3 = r3-3
			paths.append(2)
		if t8 <= 0:
			t8 = r3*t8
			t8 = t8+x
			paths.append(3)
		else:
			t8 = 8+t8
			x = x/1
			t8 = t8/x
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))