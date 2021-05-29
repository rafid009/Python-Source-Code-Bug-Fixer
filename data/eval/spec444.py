import numpy as np 

def function(x):

	k4 = 7
	s6 = x
	paths = []
	try:
		if k4 >= 5:
			x = x*4
			x = 1+x
			paths.append(1)
		else:
			k4 = k4-3
			k4 = k4*2
			paths.append(2)
		if x >= 4:
			k4 = 0/7
			x = x+7
			s6 = s6+s6
			paths.append(3)
		else:
			s6 = 6/s6
			k4 = s6/9
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		k4 = s6**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))