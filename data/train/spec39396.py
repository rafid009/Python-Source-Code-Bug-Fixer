import numpy as np 

def function(x):

	o9 = x
	s9 = 9
	paths = []
	try:
		if x < 6:
			o9 = x+1
			x = x*s9
			o9 = x+0
			paths.append(1)
		else:
			o9 = s9+0
			o9 = 0-o9
			paths.append(2)
		if s9 >= 4:
			x = 8/x
			x = x*o9
			paths.append(3)
		else:
			o9 = s9/o9
			o9 = o9*8
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		s9 = o9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))