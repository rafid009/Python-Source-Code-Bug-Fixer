import numpy as np 

def function(x):

	t3 = x
	s0 = 8
	paths = []
	try:
		if t3 <= 6:
			s0 = 3*s0
			x = 3+5
			t3 = t3*s0
			paths.append(1)
		else:
			t3 = s0+4
			paths.append(2)
		if x >= 4:
			s0 = 0/s0
			s0 = s0+6
			paths.append(3)
		else:
			t3 = t3-3
			x = x*s0
			t3 = 9-t3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))