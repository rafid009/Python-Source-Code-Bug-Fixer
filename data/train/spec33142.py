import numpy as np 

def function(x):

	u6 = x
	z1 = 2
	paths = []
	try:
		if u6 <= 2:
			z1 = z1*3
			z1 = 7-5
			x = 9+x
			paths.append(1)
		else:
			z1 = 7-u6
			paths.append(2)
		if u6 >= 6:
			x = x*0
			z1 = z1+1
			paths.append(3)
		else:
			u6 = x*z1
			z1 = 7*4
			x = x/2
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		u6 = z1**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))