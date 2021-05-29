import numpy as np 

def function(x):

	t5 = x
	s1 = 8
	paths = []
	try:
		if s1 >= 5:
			s1 = 9-s1
			s1 = 2*x
			t5 = 1*1
			paths.append(1)
		else:
			s1 = s1+s1
			paths.append(2)
		if x <= 1:
			s1 = s1/5
			paths.append(3)
		else:
			s1 = 9+5
			x = x-4
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		t5 = s1**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))