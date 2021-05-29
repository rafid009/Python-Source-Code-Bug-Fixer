import numpy as np 

def function(x):

	j8 = x
	s7 = x
	x = 4
	paths = []
	try:
		if x > 8:
			j8 = j8/7
			j8 = 9-6
			paths.append(1)
		else:
			s7 = 3/3
			x = x*3
			s7 = s7/1
			paths.append(2)
		if j8 < 5:
			s7 = 8/s7
			paths.append(3)
		else:
			x = x/j8
			s7 = s7+x
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))