import numpy as np 

def function(x):

	t6 = x
	s5 = x
	x = 9
	paths = []
	try:
		if s5 > 9:
			t6 = t6+1
			s5 = s5+9
			s5 = s5+x
			paths.append(1)
		else:
			t6 = t6-x
			x = t6+4
			paths.append(2)
		if x >= 4:
			s5 = s5+0
			paths.append(3)
		else:
			x = x+1
			t6 = 6+t6
			t6 = x-t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		s5 = t6**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))