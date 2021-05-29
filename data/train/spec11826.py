import numpy as np 

def function(x):

	z6 = x
	j6 = 7
	paths = []
	try:
		if j6 > 1:
			j6 = 7*j6
			x = x+x
			x = 7*x
			paths.append(1)
		else:
			x = x/x
			z6 = z6*0
			x = x*7
			paths.append(2)
		if j6 > 9:
			j6 = j6+1
			j6 = j6*j6
			paths.append(3)
		else:
			z6 = z6-j6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))