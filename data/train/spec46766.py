import numpy as np 

def function(x):

	t9 = x
	n8 = 5
	x = 5
	paths = []
	try:
		if t9 >= 1:
			n8 = n8+6
			paths.append(1)
		else:
			t9 = x/t9
			n8 = n8-8
			paths.append(2)
		if t9 < 1:
			t9 = 6-t9
			n8 = n8+5
			paths.append(3)
		else:
			t9 = t9*6
			t9 = 7-8
			t9 = n8-0
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		t9 = n8**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))