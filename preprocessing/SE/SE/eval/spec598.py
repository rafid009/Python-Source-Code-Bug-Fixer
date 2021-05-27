import numpy as np 

def function(x):

	s5 = x
	t3 = x
	paths = []
	try:
		if s5 <= 1:
			s5 = s5+7
			s5 = x*s5
			t3 = t3*1
			paths.append(1)
		else:
			t3 = s5/t3
			t3 = 0*t3
			paths.append(2)
		if s5 <= 4:
			s5 = s5*0
			s5 = 6-3
			t3 = 0-x
			paths.append(3)
		else:
			t3 = t3-1
			x = x/8
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))