import numpy as np 

def function(x):

	s5 = 8
	r6 = 0
	paths = []
	try:
		if x >= 7:
			s5 = s5/8
			x = 8/x
			r6 = r6*x
			paths.append(1)
		else:
			r6 = r6-3
			s5 = s5-4
			x = 3-x
			paths.append(2)
		if r6 >= 9:
			x = 7*x
			x = 2-8
			r6 = r6-x
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))