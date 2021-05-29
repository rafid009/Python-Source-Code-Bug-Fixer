import numpy as np 

def function(x):

	e5 = x
	o0 = 3
	paths = []
	try:
		if e5 <= 5:
			o0 = x/o0
			o0 = o0+x
			paths.append(1)
		else:
			x = x/o0
			o0 = o0*2
			paths.append(2)
		if x <= 3:
			o0 = e5/o0
			o0 = 8*o0
			paths.append(3)
		else:
			o0 = e5/o0
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))