import numpy as np 

def function(x):

	j1 = x
	s5 = 4
	paths = []
	try:
		if x > 7:
			x = 2+x
			x = 2+8
			paths.append(1)
		else:
			x = x-s5
			paths.append(2)
		if x < 4:
			s5 = s5*x
			x = 6*x
			j1 = j1*x
			paths.append(3)
		else:
			x = 7+s5
			j1 = j1-j1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		s5 = j1**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))