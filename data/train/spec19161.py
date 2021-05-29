import numpy as np 

def function(x):

	v9 = x
	s8 = 2
	paths = []
	try:
		if x < 2:
			x = x+5
			v9 = 4/v9
			paths.append(1)
		else:
			v9 = 4-6
			v9 = v9/9
			paths.append(2)
		if s8 > 3:
			s8 = 9*2
			s8 = s8+1
			paths.append(3)
		else:
			x = s8-7
			v9 = x-8
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))