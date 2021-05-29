import numpy as np 

def function(x):

	t9 = x
	s6 = 3
	paths = []
	try:
		if x < 3:
			t9 = 5+t9
			paths.append(1)
		else:
			t9 = 0+t9
			s6 = 0*s6
			paths.append(2)
		if s6 > 6:
			s6 = s6+0
			s6 = 1+3
			s6 = s6/x
			paths.append(3)
		else:
			x = 7/x
			x = x/6
			x = 3/3
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