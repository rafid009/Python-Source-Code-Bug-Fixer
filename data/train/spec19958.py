import numpy as np 

def function(x):

	v7 = 2
	s1 = x
	paths = []
	try:
		if v7 >= 7:
			v7 = v7-x
			x = x+4
			paths.append(1)
		else:
			x = 0/4
			paths.append(2)
		if x <= 3:
			x = s1-0
			s1 = s1-5
			v7 = 8*0
			paths.append(3)
		else:
			s1 = s1-s1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))