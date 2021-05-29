import numpy as np 

def function(x):

	v4 = x
	s2 = x
	x = 5
	paths = []
	try:
		if s2 > 4:
			s2 = s2*2
			x = 4+4
			paths.append(1)
		else:
			v4 = 3*v4
			s2 = v4-6
			x = 1/1
			paths.append(2)
		if v4 <= 7:
			v4 = v4+s2
			paths.append(3)
		else:
			s2 = s2/3
			v4 = v4+6
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))