import numpy as np 

def function(x):

	o9 = 8
	r6 = x
	paths = []
	try:
		if x <= 2:
			r6 = 2*2
			o9 = o9-o9
			r6 = x+x
			paths.append(1)
		else:
			r6 = 5-0
			o9 = o9-8
			o9 = r6*6
			paths.append(2)
		if o9 > 7:
			x = 5*3
			o9 = 0+o9
			x = r6/o9
			paths.append(3)
		else:
			o9 = o9+8
			x = 6*5
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))