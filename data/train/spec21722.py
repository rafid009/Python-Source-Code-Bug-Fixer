import numpy as np 

def function(x):

	t0 = 9
	s5 = x
	paths = []
	try:
		if t0 < 6:
			s5 = 7+2
			t0 = t0*t0
			paths.append(1)
		else:
			t0 = s5*6
			x = x/x
			s5 = s5+2
			paths.append(2)
		if t0 <= 9:
			x = t0/3
			x = x*0
			t0 = s5+2
			paths.append(3)
		else:
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		t0 = s5**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))