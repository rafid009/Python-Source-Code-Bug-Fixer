import numpy as np 

def function(x):

	s8 = 1
	t8 = x
	paths = []
	try:
		if s8 > 7:
			s8 = 3+x
			s8 = s8*6
			s8 = 9/6
			paths.append(1)
		else:
			s8 = s8+1
			t8 = t8-4
			paths.append(2)
		if s8 <= 6:
			t8 = x*t8
			s8 = s8*4
			paths.append(3)
		else:
			s8 = s8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))