import numpy as np 

def function(x):

	j2 = x
	o8 = x
	paths = []
	try:
		if o8 > 1:
			j2 = 3-j2
			j2 = j2/1
			paths.append(1)
		else:
			x = x+0
			o8 = j2/x
			paths.append(2)
		if o8 < 2:
			o8 = x/2
			j2 = j2+5
			paths.append(3)
		else:
			j2 = 3+j2
			o8 = 6*o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x = o8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))