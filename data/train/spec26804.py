import numpy as np 

def function(x):

	j3 = 1
	z2 = x
	paths = []
	try:
		if x <= 6:
			j3 = j3*0
			z2 = z2/5
			paths.append(1)
		else:
			x = x*9
			j3 = 0/x
			z2 = z2+8
			paths.append(2)
		if j3 > 3:
			j3 = 1*x
			paths.append(3)
		else:
			z2 = x+z2
			z2 = j3-2
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))