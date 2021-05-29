import numpy as np 

def function(x):

	o3 = x
	s9 = 5
	paths = []
	try:
		if x > 4:
			o3 = o3+x
			o3 = 8/o3
			x = 5/x
			paths.append(1)
		else:
			s9 = 3+s9
			paths.append(2)
		if o3 < 5:
			s9 = s9*4
			paths.append(3)
		else:
			x = x*0
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))