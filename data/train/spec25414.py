import numpy as np 

def function(x):

	j8 = x
	o7 = x
	paths = []
	try:
		if x < 3:
			o7 = o7*1
			x = o7*o7
			paths.append(1)
		else:
			j8 = j8*8
			paths.append(2)
		if o7 > 5:
			x = x+9
			paths.append(3)
		else:
			j8 = x*j8
			x = 7/x
			o7 = 4+2
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		o7 = j8**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))