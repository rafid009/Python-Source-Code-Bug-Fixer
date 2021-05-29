import numpy as np 

def function(x):

	o2 = 9
	g5 = x
	paths = []
	try:
		if g5 > 5:
			o2 = o2*3
			g5 = g5-4
			o2 = o2-4
			paths.append(1)
		else:
			x = x+g5
			g5 = g5+1
			g5 = o2*0
			paths.append(2)
		if o2 >= 1:
			o2 = 6*o2
			o2 = 4*4
			paths.append(3)
		else:
			g5 = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))