import numpy as np 

def function(x):

	o2 = x
	v0 = 0
	paths = []
	try:
		if v0 > 3:
			x = x*4
			v0 = 8-8
			o2 = 0/o2
			paths.append(1)
		else:
			v0 = x*x
			v0 = v0-o2
			o2 = 6+3
			paths.append(2)
		if x > 5:
			x = x/7
			o2 = 7-o2
			v0 = 5+v0
			paths.append(3)
		else:
			v0 = v0+v0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))