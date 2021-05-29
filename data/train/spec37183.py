import numpy as np 

def function(x):

	j9 = x
	s7 = x
	paths = []
	try:
		if s7 >= 4:
			j9 = j9/j9
			s7 = s7*j9
			s7 = j9-0
			paths.append(1)
		else:
			j9 = 2-j9
			x = s7*s7
			s7 = 5/s7
			paths.append(2)
		if x >= 6:
			j9 = j9*8
			s7 = 0+j9
			s7 = j9-6
			paths.append(3)
		else:
			j9 = j9+2
			s7 = s7/s7
			x = x+s7
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))