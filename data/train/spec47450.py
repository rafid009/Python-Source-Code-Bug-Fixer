import numpy as np 

def function(x):

	z9 = x
	k6 = 4
	paths = []
	try:
		if k6 <= 7:
			x = 5/1
			x = x/8
			paths.append(1)
		else:
			z9 = k6*0
			paths.append(2)
		if x > 3:
			x = 3-1
			paths.append(3)
		else:
			z9 = 6*z9
			k6 = 3*7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		k6 = z9**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))