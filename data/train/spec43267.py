import numpy as np 

def function(x):

	s5 = x
	j4 = 6
	paths = []
	try:
		if x >= 9:
			s5 = x/s5
			j4 = j4+6
			s5 = s5-j4
			paths.append(1)
		else:
			x = 1+x
			x = 3*x
			j4 = 8+j4
			paths.append(2)
		if x > 5:
			s5 = 7-s5
			j4 = 9*s5
			s5 = 2*6
			paths.append(3)
		else:
			x = x*4
			x = x+x
			x = 8+j4
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		j4 = s5**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))