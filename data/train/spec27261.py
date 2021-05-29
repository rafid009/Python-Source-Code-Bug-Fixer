import numpy as np 

def function(x):

	o4 = 1
	t9 = 7
	paths = []
	try:
		if x <= 2:
			o4 = 9+o4
			paths.append(1)
		else:
			t9 = t9/x
			t9 = 2-5
			t9 = t9-5
			paths.append(2)
		if t9 > 4:
			x = t9-x
			x = x+4
			t9 = 5-t9
			paths.append(3)
		else:
			t9 = 3*8
			o4 = o4+x
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))