import numpy as np 

def function(x):

	v3 = x
	z2 = 8
	paths = []
	try:
		if v3 <= 7:
			v3 = v3+6
			x = x/7
			paths.append(1)
		else:
			v3 = x+v3
			x = x*2
			z2 = z2*0
			paths.append(2)
		if z2 > 7:
			z2 = z2-7
			z2 = 2+5
			z2 = z2/3
			paths.append(3)
		else:
			z2 = 1*z2
			x = 7*1
			z2 = 9+z2
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		z2 = v3**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))