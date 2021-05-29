import numpy as np 

def function(x):

	t8 = x
	q8 = 2
	paths = []
	try:
		if t8 >= 9:
			t8 = t8+5
			t8 = t8-1
			t8 = t8+q8
			paths.append(1)
		else:
			x = x/x
			q8 = q8+t8
			t8 = 8-t8
			paths.append(2)
		if t8 > 9:
			x = x/4
			q8 = q8*5
			paths.append(3)
		else:
			x = x*8
			t8 = t8+t8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		t8 = q8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))