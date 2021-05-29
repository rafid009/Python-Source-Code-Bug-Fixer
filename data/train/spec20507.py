import numpy as np 

def function(x):

	i7 = 1
	o0 = 9
	paths = []
	try:
		if o0 > 9:
			x = x*x
			i7 = o0-4
			o0 = 1/7
			paths.append(1)
		else:
			i7 = i7/4
			o0 = x*o0
			paths.append(2)
		if i7 <= 5:
			x = 8+1
			paths.append(3)
		else:
			x = x+i7
			o0 = o0*9
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		i7 = o0**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))