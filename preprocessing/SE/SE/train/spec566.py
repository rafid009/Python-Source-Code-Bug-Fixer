import numpy as np 

def function(x):

	f9 = x
	s2 = 9
	paths = []
	try:
		if f9 > 3:
			s2 = 3-4
			paths.append(1)
		else:
			f9 = f9*5
			paths.append(2)
		if f9 <= 5:
			f9 = s2+f9
			s2 = s2/9
			f9 = 7/f9
			paths.append(3)
		else:
			f9 = f9*3
			x = 2*3
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))