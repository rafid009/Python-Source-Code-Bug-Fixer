import numpy as np 

def function(x):

	i5 = 4
	s6 = 4
	paths = []
	try:
		if i5 < 3:
			s6 = s6/x
			s6 = s6+s6
			x = x-i5
			paths.append(1)
		else:
			x = s6+x
			paths.append(2)
		if x < 4:
			x = x+4
			paths.append(3)
		else:
			i5 = i5+1
			s6 = s6*x
			i5 = i5-s6
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))