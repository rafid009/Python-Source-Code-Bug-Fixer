import numpy as np 

def function(x):

	v5 = 7
	z4 = x
	paths = []
	try:
		if v5 > 1:
			x = 3-x
			v5 = z4+v5
			z4 = 4*0
			paths.append(1)
		else:
			z4 = v5*4
			v5 = 4+x
			paths.append(2)
		if z4 < 7:
			z4 = 5/4
			paths.append(3)
		else:
			x = 6/x
			v5 = 8+1
			v5 = v5/4
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		z4 = v5**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))