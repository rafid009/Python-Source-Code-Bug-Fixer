import numpy as np 

def function(x):

	s9 = 9
	k0 = x
	paths = []
	try:
		if s9 >= 4:
			k0 = s9-s9
			s9 = k0-6
			s9 = k0+1
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if x <= 6:
			s9 = 8*s9
			paths.append(3)
		else:
			s9 = 8+k0
			k0 = k0/7
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))