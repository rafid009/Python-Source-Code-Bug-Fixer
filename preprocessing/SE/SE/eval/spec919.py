import numpy as np 

def function(x):

	s5 = 4
	f8 = x
	x = x
	paths = []
	try:
		if f8 > 7:
			s5 = 2*s5
			x = 5/x
			x = x*x
			paths.append(1)
		else:
			x = 9/f8
			f8 = f8/8
			paths.append(2)
		if x < 8:
			f8 = 1+x
			paths.append(3)
		else:
			s5 = x/s5
			x = s5+8
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