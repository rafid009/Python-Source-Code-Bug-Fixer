import numpy as np 

def function(x):

	v6 = 4
	s5 = x
	paths = []
	try:
		if s5 <= 3:
			v6 = v6-s5
			paths.append(1)
		else:
			v6 = x*v6
			s5 = 1*s5
			paths.append(2)
		if v6 > 7:
			v6 = 8-v6
			v6 = v6*7
			s5 = s5-7
			paths.append(3)
		else:
			v6 = x-8
			v6 = 7*x
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		v6 = s5**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))