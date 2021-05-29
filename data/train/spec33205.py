import numpy as np 

def function(x):

	v7 = x
	o5 = x
	paths = []
	try:
		if v7 <= 4:
			o5 = o5-7
			paths.append(1)
		else:
			x = 2+5
			paths.append(2)
		if o5 >= 8:
			v7 = v7*9
			o5 = o5+4
			v7 = v7*3
			paths.append(3)
		else:
			v7 = v7*o5
			o5 = o5-v7
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))