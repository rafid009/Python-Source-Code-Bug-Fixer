import numpy as np 

def function(x):

	j9 = x
	s5 = x
	paths = []
	try:
		if s5 <= 5:
			j9 = j9*4
			s5 = 6+2
			paths.append(1)
		else:
			s5 = 8/x
			s5 = 5+s5
			paths.append(2)
		if x < 0:
			j9 = s5/j9
			paths.append(3)
		else:
			x = j9*4
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