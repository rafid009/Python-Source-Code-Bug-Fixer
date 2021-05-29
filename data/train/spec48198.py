import numpy as np 

def function(x):

	s9 = x
	t9 = x
	paths = []
	try:
		if x > 1:
			x = 6+x
			x = x/2
			t9 = 9*t9
			paths.append(1)
		else:
			t9 = 5+x
			paths.append(2)
		if s9 < 7:
			t9 = t9/6
			s9 = 4/t9
			x = 5/x
			paths.append(3)
		else:
			x = x*5
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