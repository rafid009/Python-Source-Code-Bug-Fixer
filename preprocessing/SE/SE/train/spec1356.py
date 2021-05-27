import numpy as np 

def function(x):

	j2 = 8
	o6 = 5
	paths = []
	try:
		if o6 > 1:
			j2 = j2+2
			o6 = 2+3
			paths.append(1)
		else:
			o6 = 5*x
			paths.append(2)
		if j2 <= 8:
			j2 = j2*6
			paths.append(3)
		else:
			o6 = 1-o6
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))