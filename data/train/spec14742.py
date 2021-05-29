import numpy as np 

def function(x):

	o1 = x
	v0 = x
	paths = []
	try:
		if x <= 9:
			o1 = 3*7
			paths.append(1)
		else:
			x = x/7
			v0 = 6-x
			paths.append(2)
		if v0 < 7:
			o1 = x*6
			paths.append(3)
		else:
			o1 = o1*5
			x = o1*x
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))