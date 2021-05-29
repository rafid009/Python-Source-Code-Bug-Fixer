import numpy as np 

def function(x):

	r9 = 2
	t8 = 6
	paths = []
	try:
		if t8 <= 2:
			r9 = x/r9
			x = x/t8
			paths.append(1)
		else:
			r9 = r9/1
			r9 = r9/3
			paths.append(2)
		if x > 7:
			t8 = 4+t8
			r9 = r9-7
			t8 = 4-t8
			paths.append(3)
		else:
			x = 8-6
			t8 = t8/3
			t8 = t8/t8
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))