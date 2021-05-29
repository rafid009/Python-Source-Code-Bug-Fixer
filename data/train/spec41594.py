import numpy as np 

def function(x):

	d2 = x
	v0 = x
	x = 8
	paths = []
	try:
		if d2 < 4:
			d2 = 5-d2
			x = v0+x
			d2 = 9+d2
			paths.append(1)
		else:
			v0 = v0*0
			d2 = d2/7
			paths.append(2)
		if v0 < 8:
			d2 = d2*x
			v0 = v0*1
			paths.append(3)
		else:
			d2 = d2-d2
			d2 = d2/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))