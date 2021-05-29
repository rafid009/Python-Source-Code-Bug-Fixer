import numpy as np 

def function(x):

	t9 = 6
	s4 = 2
	x = x
	paths = []
	try:
		if t9 > 1:
			t9 = t9/6
			s4 = 6+s4
			s4 = s4*4
			paths.append(1)
		else:
			s4 = s4/5
			t9 = x-7
			t9 = t9-6
			paths.append(2)
		if x < 8:
			t9 = t9-7
			s4 = t9/t9
			paths.append(3)
		else:
			t9 = t9-0
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))