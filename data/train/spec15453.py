import numpy as np 

def function(x):

	t9 = x
	s8 = 8
	paths = []
	try:
		if x >= 0:
			t9 = t9*s8
			paths.append(1)
		else:
			s8 = s8-6
			s8 = 0/x
			paths.append(2)
		if t9 < 9:
			s8 = 7+0
			t9 = x-2
			paths.append(3)
		else:
			t9 = 2/t9
			x = 3/s8
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))