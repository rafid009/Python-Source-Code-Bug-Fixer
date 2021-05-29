import numpy as np 

def function(x):

	s5 = x
	v2 = x
	paths = []
	try:
		if v2 >= 9:
			v2 = v2+s5
			v2 = s5*9
			x = x/9
			paths.append(1)
		else:
			s5 = x*v2
			paths.append(2)
		if x < 9:
			s5 = 3+x
			paths.append(3)
		else:
			s5 = 0-s5
			s5 = s5/x
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))