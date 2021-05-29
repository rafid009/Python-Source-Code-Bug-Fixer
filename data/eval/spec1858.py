import numpy as np 

def function(x):

	s5 = x
	f2 = x
	paths = []
	try:
		if x < 7:
			s5 = 3/1
			x = 8*x
			paths.append(1)
		else:
			s5 = s5/3
			s5 = s5+f2
			x = 6+2
			paths.append(2)
		if s5 <= 9:
			f2 = 3-5
			f2 = 1+f2
			paths.append(3)
		else:
			s5 = 9/8
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))