import numpy as np 

def function(x):

	s7 = x
	r8 = 3
	paths = []
	try:
		if r8 <= 4:
			s7 = 2/2
			s7 = 8+8
			s7 = s7+9
			paths.append(1)
		else:
			x = x*0
			x = 4/x
			paths.append(2)
		if r8 > 9:
			x = x*5
			s7 = 0+2
			paths.append(3)
		else:
			s7 = 5-s7
			x = r8-2
			s7 = s7+s7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		r8 = s7**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))