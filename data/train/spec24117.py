import numpy as np 

def function(x):

	j1 = 0
	s5 = x
	paths = []
	try:
		if x > 8:
			j1 = 4+j1
			x = x*s5
			paths.append(1)
		else:
			s5 = 4/s5
			j1 = j1+x
			x = x/j1
			paths.append(2)
		if x > 8:
			x = s5-1
			paths.append(3)
		else:
			s5 = j1*s5
			x = 8+j1
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))