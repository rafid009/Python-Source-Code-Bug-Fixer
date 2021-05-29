import numpy as np 

def function(x):

	t6 = 7
	s5 = x
	paths = []
	try:
		if t6 >= 4:
			t6 = t6/1
			t6 = 1/s5
			paths.append(1)
		else:
			t6 = t6+2
			t6 = 9*t6
			x = x-t6
			paths.append(2)
		if s5 > 6:
			x = 7/x
			s5 = x*x
			paths.append(3)
		else:
			s5 = 1*5
			x = x-6
			x = x-8
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))