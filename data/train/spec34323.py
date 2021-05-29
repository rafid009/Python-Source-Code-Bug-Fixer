import numpy as np 

def function(x):

	s1 = x
	t4 = 5
	paths = []
	try:
		if s1 < 3:
			t4 = 7+4
			t4 = 2-2
			paths.append(1)
		else:
			s1 = 9+s1
			t4 = t4/s1
			t4 = s1*6
			paths.append(2)
		if x < 3:
			x = x/x
			t4 = x/2
			t4 = 4+t4
			paths.append(3)
		else:
			s1 = s1-1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))