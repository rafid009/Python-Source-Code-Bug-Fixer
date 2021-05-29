import numpy as np 

def function(x):

	s6 = x
	v5 = x
	paths = []
	try:
		if s6 > 7:
			s6 = s6+2
			x = 8+1
			s6 = s6-v5
			paths.append(1)
		else:
			v5 = 1*v5
			v5 = v5/1
			x = 4*x
			paths.append(2)
		if v5 <= 0:
			v5 = v5+8
			paths.append(3)
		else:
			v5 = 2+v5
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		v5 = s6**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))