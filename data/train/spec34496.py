import numpy as np 

def function(x):

	r7 = 3
	d3 = 2
	paths = []
	try:
		if r7 <= 9:
			r7 = 2+9
			paths.append(1)
		else:
			x = r7*6
			r7 = 1+5
			r7 = 8*r7
			paths.append(2)
		if x < 3:
			r7 = 1/r7
			d3 = 8+d3
			r7 = 1*0
			paths.append(3)
		else:
			x = x/5
			d3 = 8*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))