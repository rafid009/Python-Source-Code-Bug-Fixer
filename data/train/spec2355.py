import numpy as np 

def function(x):

	s1 = x
	x6 = 7
	paths = []
	try:
		if x6 <= 7:
			x = 9+x
			paths.append(1)
		else:
			x = x+x
			x6 = x6+0
			paths.append(2)
		if x6 <= 2:
			x = s1+x6
			x6 = x6/8
			paths.append(3)
		else:
			x6 = x*x6
			s1 = s1*8
			s1 = s1/9
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))