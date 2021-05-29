import numpy as np 

def function(x):

	v6 = 2
	r8 = x
	paths = []
	try:
		if x <= 4:
			r8 = 9/x
			paths.append(1)
		else:
			r8 = 6*8
			paths.append(2)
		if v6 < 4:
			x = 9+x
			v6 = v6*r8
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))