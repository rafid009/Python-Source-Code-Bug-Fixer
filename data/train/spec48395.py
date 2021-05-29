import numpy as np 

def function(x):

	i9 = 4
	s9 = 1
	paths = []
	try:
		if s9 <= 5:
			x = x+s9
			s9 = s9-5
			s9 = s9-s9
			paths.append(1)
		else:
			i9 = i9*6
			paths.append(2)
		if i9 >= 4:
			s9 = x+s9
			paths.append(3)
		else:
			s9 = x/9
			s9 = 9*0
			i9 = i9-i9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		i9 = s9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))