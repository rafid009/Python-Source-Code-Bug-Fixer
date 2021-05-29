import numpy as np 

def function(x):

	s9 = 0
	i4 = x
	paths = []
	try:
		if i4 < 5:
			s9 = 2+8
			x = x+x
			paths.append(1)
		else:
			i4 = 0/i4
			paths.append(2)
		if i4 >= 1:
			x = x-0
			i4 = i4/2
			x = x*0
			paths.append(3)
		else:
			s9 = x*6
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))