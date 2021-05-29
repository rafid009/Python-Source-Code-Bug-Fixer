import numpy as np 

def function(x):

	o8 = x
	i6 = 9
	paths = []
	try:
		if i6 <= 5:
			x = o8/6
			i6 = 6-5
			o8 = 0*x
			paths.append(1)
		else:
			o8 = 1/9
			i6 = 2+i6
			paths.append(2)
		if i6 > 1:
			i6 = 4+1
			o8 = o8*7
			i6 = i6-i6
			paths.append(3)
		else:
			i6 = x*i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))