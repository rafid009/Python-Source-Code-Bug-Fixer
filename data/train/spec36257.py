import numpy as np 

def function(x):

	r9 = x
	s1 = 1
	paths = []
	try:
		if r9 >= 5:
			s1 = s1-6
			r9 = x/3
			paths.append(1)
		else:
			x = r9+7
			r9 = r9+2
			paths.append(2)
		if x < 0:
			x = x*s1
			x = x/x
			paths.append(3)
		else:
			x = 3/4
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))