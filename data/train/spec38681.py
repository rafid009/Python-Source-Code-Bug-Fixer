import numpy as np 

def function(x):

	s5 = x
	f8 = 7
	paths = []
	try:
		if x <= 1:
			s5 = s5-2
			s5 = 6/s5
			paths.append(1)
		else:
			f8 = 9*s5
			paths.append(2)
		if x > 5:
			s5 = 6/s5
			paths.append(3)
		else:
			f8 = 4-9
			x = s5/5
			x = x*s5
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))