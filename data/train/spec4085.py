import numpy as np 

def function(x):

	n8 = 4
	o9 = 7
	paths = []
	try:
		if n8 < 0:
			x = x*x
			n8 = n8-1
			n8 = 2/n8
			paths.append(1)
		else:
			o9 = 5*o9
			n8 = n8-9
			x = x+9
			paths.append(2)
		if x <= 5:
			o9 = 4-o9
			x = x-6
			paths.append(3)
		else:
			o9 = n8*o9
			x = x*4
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		n8 = o9**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))