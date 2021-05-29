import numpy as np 

def function(x):

	f7 = 4
	s9 = 9
	paths = []
	try:
		if f7 < 2:
			f7 = 3+8
			paths.append(1)
		else:
			f7 = f7*6
			x = 3+x
			paths.append(2)
		if s9 > 7:
			s9 = s9+s9
			s9 = 6+x
			x = x*8
			paths.append(3)
		else:
			f7 = f7-f7
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))