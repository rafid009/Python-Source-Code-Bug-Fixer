import numpy as np 

def function(x):

	j2 = x
	s4 = x
	paths = []
	try:
		if j2 <= 4:
			s4 = s4-2
			x = 9-5
			j2 = j2+s4
			paths.append(1)
		else:
			s4 = 7*s4
			paths.append(2)
		if x > 6:
			x = 3/s4
			paths.append(3)
		else:
			x = s4+j2
			s4 = s4-j2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))