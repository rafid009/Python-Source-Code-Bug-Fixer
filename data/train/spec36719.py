import numpy as np 

def function(x):

	z9 = x
	d8 = x
	paths = []
	try:
		if d8 < 0:
			d8 = d8-x
			d8 = d8*2
			d8 = 1/5
			paths.append(1)
		else:
			x = 7/z9
			x = 4/1
			d8 = d8*2
			paths.append(2)
		if d8 <= 9:
			z9 = z9-7
			d8 = x+3
			paths.append(3)
		else:
			d8 = 5-d8
			x = 9/9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))