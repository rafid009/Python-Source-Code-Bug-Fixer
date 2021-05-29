import numpy as np 

def function(x):

	z7 = 9
	j3 = x
	paths = []
	try:
		if z7 < 5:
			x = x-6
			z7 = z7*1
			z7 = z7*z7
			paths.append(1)
		else:
			x = z7+j3
			j3 = 3+j3
			j3 = x+5
			paths.append(2)
		if z7 < 4:
			x = 0/1
			paths.append(3)
		else:
			j3 = 7-j3
			x = 8-z7
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))