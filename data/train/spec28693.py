import numpy as np 

def function(x):

	v9 = x
	s1 = x
	paths = []
	try:
		if s1 >= 7:
			s1 = 3/v9
			s1 = 0+s1
			s1 = s1+v9
			paths.append(1)
		else:
			s1 = s1-8
			s1 = s1+9
			paths.append(2)
		if v9 >= 1:
			v9 = v9-4
			s1 = s1*x
			v9 = 7*0
			paths.append(3)
		else:
			s1 = 6*s1
			s1 = 9/s1
			v9 = s1*6
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