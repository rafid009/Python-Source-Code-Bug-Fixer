import numpy as np 

def function(x):

	v0 = x
	s8 = x
	x = 9
	paths = []
	try:
		if x >= 2:
			x = 2+0
			paths.append(1)
		else:
			v0 = s8+4
			v0 = 6+8
			s8 = s8*5
			paths.append(2)
		if x < 5:
			v0 = s8-v0
			x = v0*0
			paths.append(3)
		else:
			x = s8+x
			v0 = x*2
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		x = s8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))