import numpy as np 

def function(x):

	v2 = x
	s8 = x
	paths = []
	try:
		if x >= 8:
			v2 = x/v2
			s8 = s8+3
			paths.append(1)
		else:
			x = x+4
			x = 2+s8
			x = x+1
			paths.append(2)
		if v2 > 9:
			x = 2-x
			paths.append(3)
		else:
			v2 = s8-v2
			x = 8+x
			x = x/3
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		v2 = s8**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))