import numpy as np 

def function(x):

	t6 = 3
	s6 = x
	paths = []
	try:
		if s6 <= 3:
			s6 = s6+9
			paths.append(1)
		else:
			x = x/t6
			paths.append(2)
		if x >= 3:
			x = x*3
			s6 = s6/1
			paths.append(3)
		else:
			t6 = t6+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))