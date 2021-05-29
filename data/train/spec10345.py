import numpy as np 

def function(x):

	t1 = x
	s9 = 2
	paths = []
	try:
		if x <= 0:
			s9 = s9*5
			s9 = s9+s9
			paths.append(1)
		else:
			t1 = x-t1
			s9 = 7+t1
			paths.append(2)
		if s9 > 0:
			t1 = t1+6
			s9 = s9-6
			paths.append(3)
		else:
			s9 = s9/x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))