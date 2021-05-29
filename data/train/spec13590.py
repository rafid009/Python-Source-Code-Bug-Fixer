import numpy as np 

def function(x):

	v3 = x
	s2 = 9
	paths = []
	try:
		if v3 >= 7:
			v3 = v3-v3
			x = x*0
			paths.append(1)
		else:
			s2 = 7*s2
			x = x/2
			s2 = x/8
			paths.append(2)
		if v3 <= 5:
			v3 = v3+v3
			x = 0/3
			paths.append(3)
		else:
			s2 = x/s2
			v3 = 2/v3
			v3 = s2-v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		s2 = v3**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))