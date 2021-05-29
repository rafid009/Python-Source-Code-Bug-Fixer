import numpy as np 

def function(x):

	s4 = x
	t6 = x
	paths = []
	try:
		if x >= 0:
			t6 = t6*s4
			paths.append(1)
		else:
			t6 = 9-t6
			x = 6/8
			x = s4*x
			paths.append(2)
		if x > 4:
			t6 = t6-1
			s4 = 3+7
			t6 = t6-s4
			paths.append(3)
		else:
			x = s4*1
			x = x/4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		t6 = s4**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))