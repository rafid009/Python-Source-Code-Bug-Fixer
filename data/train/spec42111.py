import numpy as np 

def function(x):

	k0 = 9
	s6 = 3
	paths = []
	try:
		if s6 < 2:
			k0 = x/s6
			x = x+7
			k0 = s6+k0
			paths.append(1)
		else:
			k0 = 2-x
			x = x-k0
			paths.append(2)
		if x >= 7:
			s6 = x+5
			k0 = 8+5
			paths.append(3)
		else:
			s6 = s6*0
			x = 0-x
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))