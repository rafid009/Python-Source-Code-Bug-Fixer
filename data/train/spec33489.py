import numpy as np 

def function(x):

	v9 = x
	s5 = x
	x = x
	paths = []
	try:
		if x > 2:
			s5 = v9/4
			x = 8*x
			paths.append(1)
		else:
			s5 = v9-v9
			x = x+4
			v9 = v9*6
			paths.append(2)
		if v9 < 5:
			s5 = x+1
			x = v9-s5
			paths.append(3)
		else:
			v9 = v9+v9
			v9 = 2-v9
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