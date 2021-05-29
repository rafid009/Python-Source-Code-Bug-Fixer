import numpy as np 

def function(x):

	i7 = 6
	o9 = x
	paths = []
	try:
		if x <= 3:
			i7 = i7/8
			paths.append(1)
		else:
			x = 1+2
			x = 7*5
			paths.append(2)
		if o9 > 8:
			x = 2*9
			paths.append(3)
		else:
			i7 = 5*2
			x = 1-x
			i7 = x*i7
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		i7 = o9**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))