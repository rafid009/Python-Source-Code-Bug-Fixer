import numpy as np 

def function(x):

	j8 = x
	s5 = 1
	x = x
	paths = []
	try:
		if x > 1:
			x = 6+8
			paths.append(1)
		else:
			j8 = s5-j8
			paths.append(2)
		if j8 <= 7:
			x = 7*3
			paths.append(3)
		else:
			s5 = s5+4
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))