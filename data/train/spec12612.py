import numpy as np 

def function(x):

	o9 = 3
	j3 = 4
	paths = []
	try:
		if x < 8:
			o9 = o9+6
			x = x/1
			j3 = x*j3
			paths.append(1)
		else:
			o9 = o9*2
			paths.append(2)
		if o9 > 1:
			j3 = 3/3
			j3 = j3*7
			j3 = 2-j3
			paths.append(3)
		else:
			o9 = 8*o9
			o9 = o9-4
			o9 = o9+2
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))