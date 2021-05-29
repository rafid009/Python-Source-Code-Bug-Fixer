import numpy as np 

def function(x):

	f3 = 3
	s1 = x
	x = x
	paths = []
	try:
		if f3 < 8:
			s1 = s1/4
			f3 = 0/2
			s1 = f3*2
			paths.append(1)
		else:
			f3 = f3/8
			paths.append(2)
		if x > 4:
			f3 = 8-x
			f3 = f3*x
			paths.append(3)
		else:
			x = x-6
			s1 = 1+s1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))