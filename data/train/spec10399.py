import numpy as np 

def function(x):

	j5 = 3
	o5 = x
	paths = []
	try:
		if x <= 7:
			o5 = o5+9
			o5 = o5*4
			paths.append(1)
		else:
			x = x/8
			x = x+9
			j5 = j5+5
			paths.append(2)
		if o5 > 3:
			x = 5+1
			j5 = j5+j5
			j5 = j5+6
			paths.append(3)
		else:
			x = j5+x
			x = x+o5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))