import numpy as np 

def function(x):

	o7 = 0
	i6 = 2
	paths = []
	try:
		if o7 < 4:
			i6 = i6+3
			i6 = x+6
			o7 = i6*1
			paths.append(1)
		else:
			i6 = i6/7
			i6 = 7*i6
			i6 = 7-i6
			paths.append(2)
		if o7 > 7:
			o7 = 4-o7
			paths.append(3)
		else:
			o7 = x*4
			x = 0/x
			x = x-o7
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		o7 = i6**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))