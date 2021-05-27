import numpy as np 

def function(x):

	s1 = x
	r8 = x
	x = 0
	paths = []
	try:
		if s1 > 1:
			s1 = 7+3
			x = s1-4
			paths.append(1)
		else:
			s1 = s1*x
			s1 = r8-6
			r8 = 3/s1
			paths.append(2)
		if x > 9:
			s1 = s1-x
			r8 = r8+r8
			paths.append(3)
		else:
			x = r8+x
			s1 = 9/5
			x = x+1
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))