import numpy as np 

def function(x):

	j3 = x
	s2 = x
	paths = []
	try:
		if j3 > 4:
			x = x+x
			x = x/j3
			s2 = 9-s2
			paths.append(1)
		else:
			x = x-2
			j3 = j3-7
			x = x+5
			paths.append(2)
		if s2 < 8:
			j3 = x/j3
			s2 = s2*7
			x = 2-x
			paths.append(3)
		else:
			x = 0/x
			s2 = 2/4
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))